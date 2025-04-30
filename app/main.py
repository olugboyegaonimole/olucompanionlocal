from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.models import Category, Synonym, ConciseExpression, WordSubstitution, Simplification, OneWordSummary, Metaphor, Simile, Idiom, Personification, Hyperbole, WisdomProverb, CulturalProverb, MotivationalProverb, HumorousProverb, TimelessSaying, InspirationalQuote, LoveFriendshipQuote, SuccessAmbitionQuote, BirthdayCelebrationQuote, LifeLessonsQuote, CommonShortSynonym, EverydayAlternative, PowerWord, ChildFriendlyWord, AnimalSimile, NatureInspiredSimile, EmotionalSimile, FunnySimile, PoeticComparison, InternetTextingAbbreviation, ScientificMedicalPrefix, BusinessCorporateAcronym, EducationalAcademicShortform, GovernmentLegalTerm, WorldLandmark, UniqueNaturalWonder, ExtremeWeatherFact, CapitalCitiesCountries, FunGeographyTrivia, GrammarEssentials, LiteraryDevices, CommonWritingMistakes, ExamTipsTricks, ReadingComprehensionStrategy, WorldHistoryEvent   # Import your models
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.data import categories
from fastapi.responses import HTMLResponse

from fuzzywuzzy import fuzz
from app.page_index import page_index  # our full-text data with names, content, and urls

from fastapi.middleware.cors import CORSMiddleware
from databases import Database
from typing import Dict, List
import os

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
   
from app.database import get_db
from app.models import *
from typing import Optional

from collections import defaultdict


app = FastAPI()

templates = Jinja2Templates(directory="templates")

# Database setup
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:2Ge0er1917!3@localhost/students_companion"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database connection

database = Database(SQLALCHEMY_DATABASE_URL)

# Global search cache
search_cache: Dict[str, List[Dict]] = {}

db_tables = [
    "synonyms", "concise_expressions", "word_substitutions", "simplifications",
    "one_word_summaries", "metaphors", "similes", "idioms", "personifications", "hyperboles",
    "wisdom_proverbs", "cultural_proverbs", "motivational_proverbs", "timeless_sayings",
    "inspirational_quotes", "love_friendship_quotes", "success_ambition_quotes", "birthday_celebration_quotes",
    "life_lessons_quotes", "simplified_vocabulary", "common_short_synonyms", "everyday_alternatives",
    "power_words", "child_friendly_words", "animal_similes", "nature_inspired_similes", "emotional_similes",
    "funny_similes", "poetic_comparisons", "internet_texting_abbreviations", "scientific_medical_prefixes",
    "business_corporate_acronyms", "educational_academic_shortforms", "government_legal_terms",
    "world_landmarks", "unique_natural_wonders", "extreme_weather_facts", "capital_cities_countries",
    "fun_geography_trivia", "grammar_essentials", "literary_devices", "common_writing_mistakes",
    "exam_tips_tricks", "reading_comprehension_strategies"
]

@app.on_event("startup")
async def startup():
    await database.connect()
    await load_search_cache()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# Load all table data into in-memory cache
async def load_search_cache():
    for table in db_tables:
        try:
            query = f"SELECT * FROM {table}"
            rows = await database.fetch_all(query)
            search_cache[table] = [dict(row) for row in rows]
        except Exception as e:
            print(f"Failed to load table {table}: {e}")

@app.get("/refresh_cache")
async def refresh_cache():
    await load_search_cache()
    return {"status": "Cache refreshed."}

# Table config mapping

table_config = {
    "synonyms": (Synonym, "synonyms.html"),
    "concise_expressions": (ConciseExpression, "concise_expressions.html"),
    "word_substitutions": (WordSubstitution, "word_substitutions.html"),
    "simplifications": (Simplification, "simplifications.html"),
    "one_word_summaries": (OneWordSummary, "one_word_summaries.html"),
    "metaphors": (Metaphor, "metaphors.html"),
    "similes": (Simile, "similes.html"),
    "idioms": (Idiom, "idioms.html"),
    "personifications": (Personification, "personifications.html"),
    "hyperboles": (Hyperbole, "hyperboles.html"),
    "wisdom_proverbs": (WisdomProverb, "wisdom_proverbs.html"),
    "cultural_proverbs": (CulturalProverb, "cultural_proverbs.html"),
    "motivational_proverbs": (MotivationalProverb, "motivational_proverbs.html"),
    "humorous_proverbs": (HumorousProverb, "humorous_proverbs.html"),
    "timeless_sayings": (TimelessSaying, "timeless_sayings.html"),
    "inspirational_quotes": (InspirationalQuote, "inspirational_quotes.html"),
    "love_friendship_quotes": (LoveFriendshipQuote, "love_friendship_quotes.html"),
    "success_ambition_quotes": (SuccessAmbitionQuote, "success_ambition_quotes.html"),
    "birthday_celebration_quotes": (BirthdayCelebrationQuote, "birthday_celebration_quotes.html"),
    "life_lessons_quotes": (LifeLessonsQuote, "life_lessons_quotes.html"),
    "common_short_synonyms": (CommonShortSynonym, "common_short_synonyms.html"),
    "everyday_alternatives": (EverydayAlternative, "everyday_alternatives.html"),
    "power_words": (PowerWord, "power_words.html"),
    "child_friendly_words": (ChildFriendlyWord, "child_friendly_words.html"),
    "animal_similes": (AnimalSimile, "animal_similes.html"),
    "nature_inspired_similes": (NatureInspiredSimile, "nature_inspired_similes.html"),
    "emotional_similes": (EmotionalSimile, "emotional_similes.html"),
    "funny_similes": (FunnySimile, "funny_similes.html"),
    "poetic_comparisons": (PoeticComparison, "poetic_comparisons.html"),
    "internet_texting_abbreviations": (InternetTextingAbbreviation, "internet_texting_abbreviations.html"),
    "scientific_medical_prefixes": (ScientificMedicalPrefix, "scientific_medical_prefixes.html"),
    "business_corporate_acronyms": (BusinessCorporateAcronym, "business_corporate_acronyms.html"),
    "educational_academic_shortforms": (EducationalAcademicShortform, "educational_academic_shortforms.html"),
    "government_legal_terms": (GovernmentLegalTerm, "government_legal_terms.html"),
    "world_landmarks": (WorldLandmark, "world_landmarks.html"),
    "world_history_events": (WorldHistoryEvent, "world_history.html"),
    "unique_natural_wonders": (UniqueNaturalWonder, "unique_natural_wonders.html"),
    "extreme_weather_facts": (ExtremeWeatherFact, "extreme_weather_facts.html"),
    "capital_cities_countries": (CapitalCitiesCountries, "capital_cities_countries.html"),
    "fun_geography_trivia": (FunGeographyTrivia, "fun_geography_trivia.html"),
    "grammar_essentials": (GrammarEssentials, "grammar_essentials.html"),
    "literary_devices": (LiteraryDevices, "literary_devices.html"),
    "common_writing_mistakes": (CommonWritingMistakes, "common_writing_mistakes.html"),
    "exam_tips_tricks": (ExamTipsTricks, "exam_tips_tricks.html"),
    "reading_comprehension_strategies": (ReadingComprehensionStrategy, "reading_comprehension_strategies.html"),
}

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "categories": categories})

# Mapping of table names to their URLs (for search page linking)
table_routes = {table: f"/{table}" for table in db_tables}

@app.get("/search", response_class=HTMLResponse)
async def search(request: Request, query: str = ""):
    results = []
    query_lower = query.lower()

    for category, items in search_cache.items():
        matched_items = []

        for item in items:
            # Try to find a meaningful field to use as the label
            label = (
                item.get("label")
                or item.get("word")
                or item.get("expression")
                or item.get("content")
                or item.get("term")
                or item.get("quote")
                or item.get("saying")
            )

            if label and query_lower in label.lower():
                matched_items.append({
                    "label": label,
                    "url": table_routes.get(category, "#")
                })

        if matched_items:
            results.append({
                "title": category.replace("_", " ").title(),
                "category": category,
                "items": matched_items
            })

    return templates.TemplateResponse(
        "search.html",
        {
            "request": request,
            "query": query,
            "results": results
        }
    )

#    if not query:
#        return templates.TemplateResponse("search.html", {"request": request, "query": query, "results": []})

@app.get("/{page_name}")
async def render_dynamic_page(request: Request, page_name: str, db: Session = Depends(get_db)):
    config = table_config.get(page_name)
    if not config:
        raise HTTPException(status_code=404, detail="Page not found")

    model, template_name = config
    data = db.query(model).all()
    context_key = page_name
    return templates.TemplateResponse(template_name, {
        "request": request,
        context_key: data
    })


