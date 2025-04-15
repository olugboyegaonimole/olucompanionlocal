from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.models import Category, Synonym, ConciseExpression, WordSubstitution, Simplification, OneWordSummary, Metaphor, Simile, Idiom, Personification, Hyperbole, WisdomProverb, CulturalProverb, MotivationalProverb, HumorousProverb, TimelessSaying, InspirationalQuote, LoveFriendshipQuote, SuccessAmbitionQuote, BirthdayCelebrationQuote   # Import your models
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi import Depends


# Initialize FastAPI app and Jinja2 templates
app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Database setup (replace with your actual database URI)
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:2Ge0er1917!3@localhost/students_companion"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def home(request: Request, db: Session = Depends(get_db)):
    # Fetch some categories or items from the database
    categories = db.query(Category).all()  # Replace with the model for categories
    return templates.TemplateResponse("index.html", {"request": request, "categories": categories})

@app.get("/synonyms")
async def view_synonyms(request: Request, db: Session = Depends(get_db)):
    # Fetch data from the synonyms table
    synonyms = db.query(Synonym).all()
    return templates.TemplateResponse("synonyms.html", {"request": request, "synonyms": synonyms})

@app.get("/concise_expressions")
async def view_concise_expressions(request: Request, db: Session = Depends(get_db)):
    expressions = db.query(ConciseExpression).all()  # Fetch all entries from concise_expressions table
    return templates.TemplateResponse("concise_expressions.html", {"request": request, "concise_expressions": expressions})

@app.get("/word_substitutions")
async def view_word_substitutions(request: Request, db: Session = Depends(get_db)):
    substitutions = db.query(WordSubstitution).all()
    return templates.TemplateResponse("word_substitutions.html", {"request": request, "word_substitutions": substitutions})

@app.get("/simplifications")
async def view_simplifications(request: Request, db: Session = Depends(get_db)):
    simplifications = db.query(Simplification).all()
    return templates.TemplateResponse("simplifications.html", {"request": request, "simplifications": simplifications})

@app.get("/one_word_summaries")
async def view_one_word_summaries(request: Request, db: Session = Depends(get_db)):
    summaries = db.query(OneWordSummary).all()
    return templates.TemplateResponse("one_word_summaries.html", {"request": request, "one_word_summaries": summaries})

@app.get("/metaphors")
async def view_metaphors(request: Request, db: Session = Depends(get_db)):
    metaphors = db.query(Metaphor).all()
    return templates.TemplateResponse("metaphors.html", {"request": request, "metaphors": metaphors})

@app.get("/similes")
async def view_similes(request: Request, db: Session = Depends(get_db)):
    similes = db.query(Simile).all()
    return templates.TemplateResponse("similes.html", {"request": request, "similes": similes})

@app.get("/idioms")
async def view_idioms(request: Request, db: Session = Depends(get_db)):
    idioms = db.query(Idiom).all()
    return templates.TemplateResponse("idioms.html", {"request": request, "idioms": idioms})

@app.get("/personifications")
async def view_personifications(request: Request, db: Session = Depends(get_db)):
    personifications = db.query(Personification).all()
    return templates.TemplateResponse("personifications.html", {"request": request, "personifications": personifications})

@app.get("/hyperboles")
async def view_hyperboles(request: Request, db: Session = Depends(get_db)):
    hyperboles = db.query(Hyperbole).all()
    return templates.TemplateResponse("hyperboles.html", {"request": request, "hyperboles": hyperboles})
    
@app.get("/wisdom_proverbs")
async def view_proverbs(request: Request, db: Session = Depends(get_db)):
    proverbs = db.query(WisdomProverb).all()
    return templates.TemplateResponse("wisdom_proverbs.html", {"request": request, "proverbs": proverbs})
    
@app.get("/cultural_proverbs")
async def view_cultural_proverbs(request: Request, db: Session = Depends(get_db)):
    cultural_proverbs = db.query(CulturalProverb).all()
    return templates.TemplateResponse("cultural_proverbs.html", {
        "request": request,
        "cultural_proverbs": cultural_proverbs
    })

@app.get("/motivational_proverbs")
async def view_motivational_proverbs(request: Request, db: Session = Depends(get_db)):
    motivational_proverbs = db.query(MotivationalProverb).all()
    return templates.TemplateResponse("motivational_proverbs.html", {
        "request": request,
        "motivational_proverbs": motivational_proverbs
    })

@app.get("/humorous_proverbs")
async def view_humorous_proverbs(request: Request, db: Session = Depends(get_db)):
    humorous_proverbs = db.query(HumorousProverb).all()
    return templates.TemplateResponse("humorous_proverbs.html", {
        "request": request,
        "humorous_proverbs": humorous_proverbs
    })

@app.get("/timeless_sayings")
async def view_timeless_sayings(request: Request, db: Session = Depends(get_db)):
    timeless_sayings = db.query(TimelessSaying).all()
    return templates.TemplateResponse("timeless_sayings.html", {
        "request": request,
        "timeless_sayings": timeless_sayings
    })

@app.get("/inspirational_quotes")
async def view_inspirational_quotes(request: Request, db: Session = Depends(get_db)):
    quotes = db.query(InspirationalQuote).all()
    return templates.TemplateResponse("inspirational_quotes.html", {
        "request": request,
        "inspirational_quotes": quotes
    })

@app.get("/love_friendship_quotes")
async def view_love_friendship_quotes(request: Request, db: Session = Depends(get_db)):
    quotes = db.query(LoveFriendshipQuote).all()
    return templates.TemplateResponse("love_friendship_quotes.html", {
        "request": request,
        "love_friendship_quotes": quotes
    })

@app.get("/success_ambition_quotes")
async def view_success_ambition_quotes(request: Request, db: Session = Depends(get_db)):
    quotes = db.query(SuccessAmbitionQuote).all()
    return templates.TemplateResponse("success_ambition_quotes.html", {
        "request": request,
        "success_ambition_quotes": quotes
    })

@app.get("/birthday_celebration_quotes")
async def view_birthday_celebration_quotes(request: Request, db: Session = Depends(get_db)):
    quotes = db.query(BirthdayCelebrationQuote).all()
    return templates.TemplateResponse("birthday_celebration_quotes.html", {
        "request": request,
        "birthday_celebration_quotes": quotes
    })