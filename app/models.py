from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    entries = relationship("Entry", back_populates="category")

class Entry(Base):
    __tablename__ = "entries"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, index=True)
    explanation = Column(String)
    category_id = Column(Integer, ForeignKey("categories.id"))

    category = relationship("Category", back_populates="entries")

# 1. Single Words for Phrases and Sentences - Synonyms
class Synonym(Base):
    __tablename__ = "synonyms"
    id = Column(Integer, primary_key=True, index=True)
    phrase = Column(String, index=True)  # Match 'phrase' from DB
    synonym = Column(String)

# 2. Single Words for Phrases and Sentences - Concise Expressions
class ConciseExpression(Base):
    __tablename__ = "concise_expressions"  # This should match the table name in your database
    
    id = Column(Integer, primary_key=True, index=True)
    phrase = Column(String, nullable=False)  # The phrase column
    concise_version = Column(String, nullable=False)  # The concise version column

# 3. Single Words for Phrases and Sentences - Word Substitutions
class WordSubstitution(Base):
    __tablename__ = "word_substitutions"
    
    id = Column(Integer, primary_key=True, index=True)
    original_word = Column(String)
    replacement = Column(String)

# 4. Single Words for Phrases and Sentences - Simplifications
class Simplification(Base):
    __tablename__ = "simplifications"
    
    id = Column(Integer, primary_key=True, index=True)
    complex_expression = Column(String)
    simple_alternative = Column(String)

# 5. Single Words for Phrases and Sentences - One-Word Summaries
class OneWordSummary(Base):
    __tablename__ = "one_word_summaries"
    
    id = Column(Integer, primary_key=True, index=True)
    phrase = Column(String)
    one_word = Column(String)

# 6. Figurative Expressions - Metaphors
class Metaphor(Base):
    __tablename__ = "metaphors"
    
    id = Column(Integer, primary_key=True, index=True)
    metaphor = Column(String)
    meaning = Column(String)

# 7. Figurative Expressions - Similes
class Simile(Base):
    __tablename__ = "similes"
    id = Column(Integer, primary_key=True, index=True)
    simile = Column(String, index=True)
    meaning = Column(String)

# 8. Figurative Expressions - Idioms
class Idiom(Base):
    __tablename__ = "idioms"
    
    id = Column(Integer, primary_key=True, index=True)
    idiom = Column(String)
    meaning = Column(String)

# 9. Figurative Expressions - Personifications
class Personification(Base):
    __tablename__ = "personifications"
    id = Column(Integer, primary_key=True, index=True)
    phrase = Column(String, index=True)
    meaning = Column(String)

# 10. Figurative Expressions - Hyperboles
class Hyperbole(Base):
    __tablename__ = "hyperboles"
    id = Column(Integer, primary_key=True, index=True)
    phrase = Column(String, index=True)
    meaning = Column(String)

# 11. Proverbs - Wisdom Proverbs
class WisdomProverb(Base):
    __tablename__ = "wisdom_proverbs"
    id = Column(Integer, primary_key=True, index=True)
    proverb = Column(String, index=True)
    meaning = Column(String)

# 12. Proverbs - Cultural Proverbs
class CulturalProverb(Base):
    __tablename__ = "cultural_proverbs"
    
    id = Column(Integer, primary_key=True, index=True)
    proverb = Column(String)
    origin = Column(String)
    meaning = Column(String)

# 13. Proverbs - Motivational Proverbs
class MotivationalProverb(Base):
    __tablename__ = "motivational_proverbs"
    
    id = Column(Integer, primary_key=True, index=True)
    proverb = Column(String)
    meaning = Column(String)

# 14. Proverbs - Humorous Proverbs
class HumorousProverb(Base):
    __tablename__ = "humorous_proverbs"
    
    id = Column(Integer, primary_key=True, index=True)
    proverb = Column(String)
    meaning = Column(String)

# 15. Proverbs - Timeless Sayings
class TimelessSaying(Base):
    __tablename__ = "timeless_sayings"
    
    id = Column(Integer, primary_key=True, index=True)
    saying = Column(String)
    meaning = Column(String)

# 16. 100 Choice Quotations - Inspirational Quotes
class InspirationalQuote(Base):
    __tablename__ = "inspirational_quotes"
    
    id = Column(Integer, primary_key=True, index=True)
    quote = Column(String)
    author = Column(String)

# 17. 100 Choice Quotations - Love & Friendship Quotes
class LoveFriendshipQuote(Base):
    __tablename__ = "love_friendship_quotes"
    
    id = Column(Integer, primary_key=True, index=True)
    quote = Column(String)
    author = Column(String)

# 18. 100 Choice Quotations - Success & Ambition Quotes
class SuccessAmbitionQuote(Base):
    __tablename__ = "success_ambition_quotes"
    
    id = Column(Integer, primary_key=True, index=True)
    quote = Column(String)
    author = Column(String)

# 19. 100 Choice Quotations - Birthday & Celebration Quotes
class BirthdayCelebrationQuote(Base):
    __tablename__ = "birthday_celebration_quotes"
    
    id = Column(Integer, primary_key=True, index=True)
    quote = Column(String)
    author = Column(String)

# 20. 100 Choice Quotations - Quotes on Life Lessons
class LifeLessonsQuote(Base):
    __tablename__ = "life_lessons_quotes"
    
    id = Column(Integer, primary_key=True, index=True)
    quote = Column(String)
    author = Column(String)

# 21. Small Words for Big Ones - Simplified Vocabulary
class SimplifiedVocabulary(Base):
    __tablename__ = "simplified_vocabulary"
    
    id = Column(Integer, primary_key=True, index=True)
    word = Column(String)
    simplified_version = Column(String)

# 22. Small Words for Big Ones - Common Short Synonyms
class CommonShortSynonym(Base):
    __tablename__ = "common_short_synonyms"
    
    id = Column(Integer, primary_key=True, index=True)
    complex_word = Column(String)
    simpler_word = Column(String)

# 23. Small Words for Big Ones - Everyday Alternatives
class EverydayAlternative(Base):
    __tablename__ = "everyday_alternatives"
    
    id = Column(Integer, primary_key=True, index=True)
    formal_word  = Column(String)
    informal_alternative  = Column(String)

# 24. Small Words for Big Ones - Power Words
class PowerWord(Base):
    __tablename__ = "power_words"
    
    id = Column(Integer, primary_key=True, index=True)
    word = Column(String)
    usage_example  = Column(String)

# 25. Small Words for Big Ones - Child-Friendly Words
class ChildFriendlyWord(Base):
    __tablename__ = "child_friendly_words"
    
    id = Column(Integer, primary_key=True, index=True)
    difficult_word  = Column(String)
    easy_word  = Column(String)

# 26. Comparisons or Similes - Animal Similes
class AnimalSimile(Base):
    __tablename__ = "animal_similes"
    
    id = Column(Integer, primary_key=True, index=True)
    simile = Column(String)
    meaning = Column(String)

# 27. Comparisons or Similes - Nature-Inspired Similes
class NatureInspiredSimile(Base):
    __tablename__ = "nature_inspired_similes"
    
    id = Column(Integer, primary_key=True, index=True)
    simile = Column(String)
    meaning = Column(String)

# 28. Comparisons or Similes - Emotional Similes
class EmotionalSimile(Base):
    __tablename__ = "emotional_similes"
    
    id = Column(Integer, primary_key=True, index=True)
    simile = Column(String)
    meaning  = Column(String)

# 29. Comparisons or Similes - Funny Similes
class FunnySimile(Base):
    __tablename__ = "funny_similes"
    
    id = Column(Integer, primary_key=True, index=True)
    simile = Column(String)
    meaning  = Column(String)

# 30. Comparisons or Similes - Poetic Comparisons
class PoeticComparison(Base):
    __tablename__ = "poetic_comparisons"
    
    id = Column(Integer, primary_key=True, index=True)
    comparison = Column(String)
    meaning  = Column(String)

# 31. Abbreviations/Prefixes - Internet & Texting Abbreviations
class InternetTextingAbbreviation(Base):
    __tablename__ = "internet_texting_abbreviations"
    
    id = Column(Integer, primary_key=True, index=True)
    abbreviation = Column(String)
    meaning = Column(String)

# 32. Abbreviations/Prefixes - Scientific & Medical Prefixes
class ScientificMedicalPrefix(Base):
    __tablename__ = "scientific_medical_prefixes"
    
    id = Column(Integer, primary_key=True, index=True)
    prefix = Column(String)
    meaning = Column(String)

# 33. Abbreviations/Prefixes - Business & Corporate Acronyms
class BusinessCorporateAcronym(Base):
    __tablename__ = "business_corporate_acronyms"
    
    id = Column(Integer, primary_key=True, index=True)
    acronym = Column(String)
    meaning = Column(String)

# 34. Abbreviations/Prefixes - Educational & Academic Shortforms
class EducationalAcademicShortform(Base):
    __tablename__ = "educational_academic_shortforms"
    
    id = Column(Integer, primary_key=True, index=True)
    abbreviation = Column(String)
    meaning = Column(String)

# 35. Abbreviations/Prefixes - Government & Legal Terms
class GovernmentLegalTerm(Base):
    __tablename__ = "government_legal_terms"
    
    id = Column(Integer, primary_key=True, index=True)
    term  = Column(String)
    meaning = Column(String)

# 36. Geographical Facts - World Landmarks
class WorldLandmark(Base):
    __tablename__ = "world_landmarks"
    
    id = Column(Integer, primary_key=True, index=True)
    landmark = Column(String)
    location = Column(String)
    fact = Column(String)

# 37. Geographical Facts - Unique Natural Wonders
class UniqueNaturalWonder(Base):
    __tablename__ = "unique_natural_wonders"
    
    id = Column(Integer, primary_key=True, index=True)
    wonder = Column(String)
    location = Column(String)
    fact = Column(String)

# 38. Geographical Facts - Extreme Weather Facts
class ExtremeWeatherFact(Base):
    __tablename__ = "extreme_weather_facts"
    
    id = Column(Integer, primary_key=True, index=True)
    phenomenon  = Column(String)
    location = Column(String)
    fact = Column(String)

# 39. Geographical Facts - Capital Cities & Countries
class CapitalCitiesCountries(Base):
    __tablename__ = "capital_cities_countries"
    
    id = Column(Integer, primary_key=True, index=True)
    capital_city  = Column(String)
    country = Column(String)

# 40. Geographical Facts - Fun Geography Trivia
class FunGeographyTrivia(Base):
    __tablename__ = "fun_geography_trivia"
    
    id = Column(Integer, primary_key=True, index=True)
    fact  = Column(String)

# 41. Revision Notes in English - Grammar Essentials
class GrammarEssentials(Base):
    __tablename__ = "grammar_essentials"
    
    id = Column(Integer, primary_key=True, index=True)
    topic  = Column(String)
    explanation  = Column(String)

# 42. Revision Notes in English - Literary Devices
class LiteraryDevices(Base):
    __tablename__ = "literary_devices"
    
    id = Column(Integer, primary_key=True, index=True)
    device = Column(String)
    definition  = Column(String)

# 43. Revision Notes in English - Common Writing Mistakes
class CommonWritingMistakes(Base):
    __tablename__ = "common_writing_mistakes"
    
    id = Column(Integer, primary_key=True, index=True)
    mistake = Column(String)
    correction  = Column(String)

# 44. Revision Notes in English - Exam Tips & Tricks
class ExamTipsTricks(Base):
    __tablename__ = "exam_tips_tricks"
    
    id = Column(Integer, primary_key=True, index=True)
    tip = Column(String)

# 45. Revision Notes in English - Reading Comprehension Strategies
class ReadingComprehensionStrategy(Base):
    __tablename__ = "reading_comprehension_strategies"
    
    id = Column(Integer, primary_key=True, index=True)
    strategy = Column(String)
    explanation = Column(String)


