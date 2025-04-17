import requests
from bs4 import BeautifulSoup
from sqlalchemy import create_engine, Column, Integer, String, Text
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import re
from urllib.parse import quote
from dotenv import load_dotenv
from sqlalchemy.orm import declarative_base


# --- Load environment variables
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

# --- Set up SQLAlchemy
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()
Base = declarative_base()

# --- Define the table model
class WorldHistoryEvent(Base):
    __tablename__ = "world_history_events"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    description = Column(Text)
    source_url = Column(String(255))

Base.metadata.create_all(bind=engine)

# --- Constants
WIKIPEDIA_BASE = "https://en.wikipedia.org/wiki/"
DEFAULT_SOURCE = "https://en.wikipedia.org/wiki/Dates_of_Epoch-Making_Events"

# --- Utility functions

def clean_title(raw_title):
    # Remove footnotes like [2]
    title = re.sub(r'\[\d+\]', '', raw_title)

    # Remove (parenthetical notes)
    title = re.sub(r'\([^)]*\)', '', title)

    # Remove trailing punctuation
    title = re.sub(r'\.+$', '', title)

    # Add spacing between glued-together words
    title = re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', title)

    # Fix things like 'Athensof' → 'Athens of'
    title = re.sub(r'([a-zA-Z])of', r'\1 of', title)

    # Collapse multiple spaces
    title = re.sub(r'\s+', ' ', title)

    return title.strip()


def generate_wikipedia_url(title):
    cleaned = clean_title(title)
    slug = quote(cleaned.replace(' ', '_'))
    return f"{WIKIPEDIA_BASE}{slug}"

def verify_url_exists(url):
    try:
        response = requests.get(url, allow_redirects=True, timeout=5)
        if response.status_code != 200:
            return False

        soup = BeautifulSoup(response.text, "html.parser")
        page_title = soup.find("title")
        if not page_title:
            return False
        title_text = page_title.text.strip().lower()

        if "does not have an article" in title_text or "search results" in title_text:
            return False
        return True
    except requests.RequestException:
        return False


# --- Scraping function
def fetch_world_history_events():
    url = "https://en.wikipedia.org/wiki/Dates_of_Epoch-Making_Events"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    events = []
    content_div = soup.find("div", class_="mw-parser-output")
    if not content_div:
        print("Could not find the content section.")
        return events

    for li in content_div.find_all("li"):
        text = li.get_text(strip=True)
        if not text or len(text) < 5:
            continue

        # Skip malformed reference notes
        if text.startswith("^"):
            print(f"[SKIP ^] {text}")
            continue

        # Separate title and description
        if "–" in text:
            title, description = map(str.strip, text.split("–", 1))
        elif ":" in text:
            title, description = map(str.strip, text.split(":", 1))
        else:
            title = text
            description = ""

        cleaned_title = clean_title(title)

        # Skip excessively long or obviously bad titles
        if len(cleaned_title) > 100:
            print(f"[SKIP LONG] {cleaned_title}")
            continue

        candidate_url = generate_wikipedia_url(cleaned_title)
        if verify_url_exists(candidate_url):
            final_url = candidate_url
            events.append({
                "title": cleaned_title,
                "description": description,
                "source_url": final_url
            })
        else:
            print(f"[INVALID] {candidate_url}")


    return events


# --- Insert into DB (avoids duplicates)
def insert_events(events):
    for event in events:
        exists = session.query(WorldHistoryEvent).filter_by(
            title=event["title"],
            description=event["description"]
        ).first()
        if not exists:
            session.add(WorldHistoryEvent(**event))
    session.commit()

# --- Main execution
if __name__ == "__main__":
    print("Fetching world history events...")
    events = fetch_world_history_events()
    print(f"Fetched {len(events)} events. Inserting into database...")
    insert_events(events)
    print("Done!")
