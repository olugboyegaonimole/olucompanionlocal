from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.models import Category, Synonym, ConciseExpression, WordSubstitution, Simplification, OneWordSummary, Metaphor, Simile, Idiom, Personification, Hyperbole, WisdomProverb, CulturalProverb, MotivationalProverb, HumorousProverb, TimelessSaying, InspirationalQuote, LoveFriendshipQuote, SuccessAmbitionQuote, BirthdayCelebrationQuote, LifeLessonsQuote, CommonShortSynonym, EverydayAlternative, PowerWord, ChildFriendlyWord, AnimalSimile, NatureInspiredSimile, EmotionalSimile, FunnySimile, PoeticComparison, InternetTextingAbbreviation, ScientificMedicalPrefix, BusinessCorporateAcronym, EducationalAcademicShortform, GovernmentLegalTerm, WorldLandmark, UniqueNaturalWonder, ExtremeWeatherFact, CapitalCitiesCountries, FunGeographyTrivia, GrammarEssentials, LiteraryDevices, CommonWritingMistakes, ExamTipsTricks, ReadingComprehensionStrategy   # Import your models
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
    # Fetch categories from the database (you should have a Category model or any other model as needed)
    categories = {
        "Single Words for Phrases and Sentences": [
            {"name": "Synonyms", "url": "/synonyms"},
            {"name": "Concise Expressions", "url": "/concise_expressions"},
            {"name": "Word Substitutions", "url": "/word_substitutions"},
            {"name": "Simplifications", "url": "/simplifications"},
            {"name": "One-Word Summaries", "url": "/one_word_summaries"}
        ],
        "Figurative Expressions and Their Explanations": [
            {"name": "Metaphors", "url": "/metaphors"},
            {"name": "Similes", "url": "/similes"},
            {"name": "Idioms", "url": "/idioms"},
            {"name": "Personifications", "url": "/personifications"},
            {"name": "Hyperboles", "url": "/hyperboles"}
        ],
        "Proverbs": [
            {"name": "Wisdom Proverbs", "url": "/wisdom_proverbs"},
            {"name": "Cultural Proverbs", "url": "/cultural_proverbs"},
            {"name": "Motivational Proverbs", "url": "/motivational_proverbs"},
            {"name": "Humorous Proverbs", "url": "/humorous_proverbs"},
            {"name": "Timeless Sayings", "url": "/timeless_sayings"}
        ],
        "100 Choice Quotations for Special Occasions": [
            {"name": "Inspirational Quotes", "url": "/inspirational_quotes"},
            {"name": "Love & Friendship Quotes", "url": "/love_friendship_quotes"},
            {"name": "Success & Ambition Quotes", "url": "/success_ambition_quotes"},
            {"name": "Birthday & Celebration Quotes", "url": "/birthday_celebration_quotes"},
            {"name": "Quotes on Life Lessons", "url": "/life_lessons_quotes"}
        ],
        "Small Words for Big Ones": [
            {"name": "Common Short Synonyms", "url": "/common_short_synonyms"},
            {"name": "Everyday Alternatives", "url": "/everyday_alternatives"},
            {"name": "Power Words", "url": "/power_words"},
            {"name": "Child-Friendly Words", "url": "/child_friendly_words"}
        ],
        "Comparisons or Similes": [
            {"name": "Animal Similes", "url": "/animal_similes"},
            {"name": "Nature-Inspired Similes", "url": "/nature_inspired_similes"},
            {"name": "Emotional Similes", "url": "/emotional_similes"},
            {"name": "Funny Similes", "url": "/funny_similes"},
            {"name": "Poetic Comparisons", "url": "/poetic_comparisons"}
        ],
        "Abbreviations/Prefixes in Common Use": [
            {"name": "Internet & Texting Abbreviations", "url": "/internet_texting_abbreviations"},
            {"name": "Scientific & Medical Prefixes", "url": "/scientific_medical_prefixes"},
            {"name": "Business & Corporate Acronyms", "url": "/business_corporate_acronyms"},
            {"name": "Educational & Academic Shortforms", "url": "/educational_academic_shortforms"},
            {"name": "Government & Legal Terms", "url": "/government_legal_terms"}
        ],
        "Some Geographical Facts Worth Remembering": [
            {"name": "World Landmarks", "url": "/world_landmarks"},
            {"name": "Unique Natural Wonders", "url": "/unique_natural_wonders"},
            {"name": "Extreme Weather Facts", "url": "/extreme_weather_facts"},
            {"name": "Capital Cities & Countries", "url": "/capital_cities_countries"},
            {"name": "Fun Geography Trivia", "url": "/fun_geography_trivia"}
        ],
        "Revision Notes in English": [
            {"name": "Grammar Essentials", "url": "/grammar_essentials"},
            {"name": "Literary Devices", "url": "/literary_devices"},
            {"name": "Common Writing Mistakes", "url": "/common_writing_mistakes"},
            {"name": "Exam Tips & Tricks", "url": "/exam_tips_tricks"},
            {"name": "Reading Comprehension Strategies", "url": "/reading_comprehension_strategies"}
        ]
    }

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

@app.get("/life_lessons_quotes")
async def view_life_lessons_quotes(request: Request, db: Session = Depends(get_db)):
    quotes = db.query(LifeLessonsQuote).all()
    return templates.TemplateResponse("life_lessons_quotes.html", {
        "request": request,
        "life_lessons_quotes": quotes
    })

@app.get("/common_short_synonyms")
async def view_common_short_synonyms(request: Request, db: Session = Depends(get_db)):
    synonyms = db.query(CommonShortSynonym).all()
    return templates.TemplateResponse("common_short_synonyms.html", {
        "request": request,
        "common_short_synonyms": synonyms
    })

@app.get("/everyday_alternatives")
async def view_everyday_alternatives(request: Request, db: Session = Depends(get_db)):
    alternatives = db.query(EverydayAlternative).all()  # Fetch all data from the everyday_alternatives table
    return templates.TemplateResponse("everyday_alternatives.html", {
        "request": request,
        "everyday_alternatives": alternatives
    })

@app.get("/power_words")
async def view_power_words(request: Request, db: Session = Depends(get_db)):
    power_words = db.query(PowerWord).all()  # Fetch all data from the power_words table
    return templates.TemplateResponse("power_words.html", {
        "request": request,
        "power_words": power_words
    })

@app.get("/child_friendly_words")
async def view_child_friendly_words(request: Request, db: Session = Depends(get_db)):
    child_friendly_words = db.query(ChildFriendlyWord).all()  # Fetch all data from the child_friendly_words table
    return templates.TemplateResponse("child_friendly_words.html", {
        "request": request,
        "child_friendly_words": child_friendly_words
    })

@app.get("/animal_similes")
async def view_animal_similes(request: Request, db: Session = Depends(get_db)):
    animal_similes = db.query(AnimalSimile).all()
    return templates.TemplateResponse("animal_similes.html", {
        "request": request,
        "animal_similes": animal_similes
    })

@app.get("/nature_inspired_similes")
async def view_nature_inspired_similes(request: Request, db: Session = Depends(get_db)):
    nature_inspired_similes = db.query(NatureInspiredSimile).all()
    return templates.TemplateResponse("nature_inspired_similes.html", {
        "request": request,
        "nature_inspired_similes": nature_inspired_similes
    })

@app.get("/emotional_similes")
async def view_emotional_similes(request: Request, db: Session = Depends(get_db)):
    emotional_similes = db.query(EmotionalSimile).all()
    return templates.TemplateResponse("emotional_similes.html", {
        "request": request,
        "emotional_similes": emotional_similes
    })

@app.get("/funny_similes")
async def view_funny_similes(request: Request, db: Session = Depends(get_db)):
    funny_similes = db.query(FunnySimile).all()
    return templates.TemplateResponse("funny_similes.html", {
        "request": request,
        "funny_similes": funny_similes
    })

@app.get("/poetic_comparisons")
async def view_poetic_comparisons(request: Request, db: Session = Depends(get_db)):
    poetic_comparisons = db.query(PoeticComparison).all()
    return templates.TemplateResponse("poetic_comparisons.html", {
        "request": request,
        "poetic_comparisons": poetic_comparisons
    })

@app.get("/internet_texting_abbreviations")
async def view_internet_texting_abbreviations(request: Request, db: Session = Depends(get_db)):
    abbreviations = db.query(InternetTextingAbbreviation).all()
    return templates.TemplateResponse("internet_texting_abbreviations.html", {
        "request": request,
        "internet_texting_abbreviations": abbreviations
    })

@app.get("/scientific_medical_prefixes")
async def view_scientific_medical_prefixes(request: Request, db: Session = Depends(get_db)):
    prefixes = db.query(ScientificMedicalPrefix).all()
    return templates.TemplateResponse("scientific_medical_prefixes.html", {
        "request": request,
        "scientific_medical_prefixes": prefixes
    })

@app.get("/business_corporate_acronyms")
async def view_business_corporate_acronyms(request: Request, db: Session = Depends(get_db)):
    acronyms = db.query(BusinessCorporateAcronym).all()
    return templates.TemplateResponse("business_corporate_acronyms.html", {
        "request": request,
        "business_corporate_acronyms": acronyms
    })

@app.get("/educational_academic_shortforms")
async def view_educational_academic_shortforms(request: Request, db: Session = Depends(get_db)):
    shortforms = db.query(EducationalAcademicShortform).all()
    return templates.TemplateResponse("educational_academic_shortforms.html", {
        "request": request,
        "educational_academic_shortforms": shortforms
    })

@app.get("/government_legal_terms")
async def view_government_legal_terms(request: Request, db: Session = Depends(get_db)):
    terms = db.query(GovernmentLegalTerm).all()
    return templates.TemplateResponse("government_legal_terms.html", {
        "request": request,
        "government_legal_terms": terms
    })

@app.get("/world_landmarks")
async def view_world_landmarks(request: Request, db: Session = Depends(get_db)):
    landmarks = db.query(WorldLandmark).all()
    return templates.TemplateResponse("world_landmarks.html", {
        "request": request,
        "world_landmarks": landmarks
    })

@app.get("/unique_natural_wonders")
async def view_unique_natural_wonders(request: Request, db: Session = Depends(get_db)):
    wonders = db.query(UniqueNaturalWonder).all()
    return templates.TemplateResponse("unique_natural_wonders.html", {
        "request": request,
        "unique_natural_wonders": wonders
    })

@app.get("/extreme_weather_facts")
async def view_extreme_weather_facts(request: Request, db: Session = Depends(get_db)):
    facts = db.query(ExtremeWeatherFact).all()
    return templates.TemplateResponse("extreme_weather_facts.html", {
        "request": request,
        "extreme_weather_facts": facts
    })

@app.get("/capital_cities_countries")
async def view_capital_cities_countries(request: Request, db: Session = Depends(get_db)):
    cities = db.query(CapitalCitiesCountries).all()
    return templates.TemplateResponse("capital_cities_countries.html", {
        "request": request,
        "capital_cities_countries": cities
    })

@app.get("/fun_geography_trivia")
async def view_fun_geography_trivia(request: Request, db: Session = Depends(get_db)):
    trivia_list = db.query(FunGeographyTrivia).all()
    return templates.TemplateResponse("fun_geography_trivia.html", {
        "request": request,
        "fun_geography_trivia": trivia_list
    })

@app.get("/grammar_essentials")
async def view_grammar_essentials(request: Request, db: Session = Depends(get_db)):
    grammar_items = db.query(GrammarEssentials).all()
    return templates.TemplateResponse("grammar_essentials.html", {
        "request": request,
        "grammar_essentials": grammar_items
    })

@app.get("/literary_devices")
async def view_literary_devices(request: Request, db: Session = Depends(get_db)):
    devices = db.query(LiteraryDevices).all()
    return templates.TemplateResponse("literary_devices.html", {
        "request": request,
        "literary_devices": devices
    })

@app.get("/common_writing_mistakes")
async def view_common_writing_mistakes(request: Request, db: Session = Depends(get_db)):
    mistakes = db.query(CommonWritingMistakes).all()
    return templates.TemplateResponse("common_writing_mistakes.html", {
        "request": request,
        "common_writing_mistakes": mistakes
    })

@app.get("/exam_tips_tricks")
async def view_exam_tips_tricks(request: Request, db: Session = Depends(get_db)):
    tips = db.query(ExamTipsTricks).all()
    return templates.TemplateResponse("exam_tips_tricks.html", {
        "request": request,
        "exam_tips_tricks": tips
    })

@app.get("/reading_comprehension_strategies")
async def view_reading_comprehension_strategies(request: Request, db: Session = Depends(get_db)):
    strategies = db.query(ReadingComprehensionStrategy).all()
    return templates.TemplateResponse("reading_comprehension_strategies.html", {
        "request": request,
        "reading_comprehension_strategies": strategies
    })
