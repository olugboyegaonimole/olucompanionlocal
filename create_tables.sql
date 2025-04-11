-- Drop all existing tables if they exist
DO $$ 
DECLARE 
    r RECORD;
BEGIN 
    FOR r IN (SELECT tablename FROM pg_tables WHERE schemaname = 'public') LOOP 
        EXECUTE 'DROP TABLE IF EXISTS ' || quote_ident(r.tablename) || ' CASCADE';
    END LOOP;
END $$;

-- 1. Single Words for Phrases and Sentences
CREATE TABLE synonyms (
    id SERIAL PRIMARY KEY,
    phrase TEXT NOT NULL,
    synonym TEXT NOT NULL
);

CREATE TABLE concise_expressions (
    id SERIAL PRIMARY KEY,
    phrase TEXT NOT NULL,
    concise_version TEXT NOT NULL
);

CREATE TABLE word_substitutions (
    id SERIAL PRIMARY KEY,
    original_word TEXT NOT NULL,
    replacement TEXT NOT NULL
);

CREATE TABLE simplifications (
    id SERIAL PRIMARY KEY,
    complex_expression TEXT NOT NULL,
    simple_alternative TEXT NOT NULL
);

CREATE TABLE one_word_summaries (
    id SERIAL PRIMARY KEY,
    phrase TEXT NOT NULL,
    one_word TEXT NOT NULL
);

-- 2. Figurative Expressions and Their Explanations
CREATE TABLE metaphors (
    id SERIAL PRIMARY KEY,
    metaphor TEXT NOT NULL,
    meaning TEXT NOT NULL
);

CREATE TABLE similes (
    id SERIAL PRIMARY KEY,
    simile TEXT NOT NULL,
    meaning TEXT NOT NULL
);

CREATE TABLE idioms (
    id SERIAL PRIMARY KEY,
    idiom TEXT NOT NULL,
    meaning TEXT NOT NULL
);

CREATE TABLE personifications (
    id SERIAL PRIMARY KEY,
    phrase TEXT NOT NULL,
    meaning TEXT NOT NULL
);

CREATE TABLE hyperboles (
    id SERIAL PRIMARY KEY,
    phrase TEXT NOT NULL,
    meaning TEXT NOT NULL
);

-- 3. Proverbs
CREATE TABLE wisdom_proverbs (
    id SERIAL PRIMARY KEY,
    proverb TEXT NOT NULL,
    meaning TEXT NOT NULL
);

CREATE TABLE cultural_proverbs (
    id SERIAL PRIMARY KEY,
    proverb TEXT NOT NULL,
    origin TEXT,
    meaning TEXT NOT NULL
);

CREATE TABLE motivational_proverbs (
    id SERIAL PRIMARY KEY,
    proverb TEXT NOT NULL,
    meaning TEXT NOT NULL
);

CREATE TABLE humorous_proverbs (
    id SERIAL PRIMARY KEY,
    proverb TEXT NOT NULL,
    meaning TEXT NOT NULL
);

CREATE TABLE timeless_sayings (
    id SERIAL PRIMARY KEY,
    saying TEXT NOT NULL,
    meaning TEXT NOT NULL
);

-- 4. 100 Choice Quotations for Special Occasions
CREATE TABLE inspirational_quotes (
    id SERIAL PRIMARY KEY,
    quote TEXT NOT NULL,
    author TEXT
);

CREATE TABLE love_friendship_quotes (
    id SERIAL PRIMARY KEY,
    quote TEXT NOT NULL,
    author TEXT
);

CREATE TABLE success_ambition_quotes (
    id SERIAL PRIMARY KEY,
    quote TEXT NOT NULL,
    author TEXT
);

CREATE TABLE birthday_celebration_quotes (
    id SERIAL PRIMARY KEY,
    quote TEXT NOT NULL,
    author TEXT
);

CREATE TABLE life_lessons_quotes (
    id SERIAL PRIMARY KEY,
    quote TEXT NOT NULL,
    author TEXT
);

-- 5. Small Words for Big Ones
CREATE TABLE simplified_vocabulary (
    id SERIAL PRIMARY KEY,
    complex_word TEXT NOT NULL,
    simple_word TEXT NOT NULL
);

CREATE TABLE common_short_synonyms (
    id SERIAL PRIMARY KEY,
    complex_word TEXT NOT NULL,
    simpler_word TEXT NOT NULL
);

CREATE TABLE everyday_alternatives (
    id SERIAL PRIMARY KEY,
    formal_word TEXT NOT NULL,
    informal_alternative TEXT NOT NULL
);

CREATE TABLE power_words (
    id SERIAL PRIMARY KEY,
    word TEXT NOT NULL,
    usage_example TEXT NOT NULL
);

CREATE TABLE child_friendly_words (
    id SERIAL PRIMARY KEY,
    difficult_word TEXT NOT NULL,
    easy_word TEXT NOT NULL
);

-- 6. Comparisons or Similes
CREATE TABLE animal_similes (
    id SERIAL PRIMARY KEY,
    simile TEXT NOT NULL,
    meaning TEXT NOT NULL
);

CREATE TABLE nature_inspired_similes (
    id SERIAL PRIMARY KEY,
    simile TEXT NOT NULL,
    meaning TEXT NOT NULL
);

CREATE TABLE emotional_similes (
    id SERIAL PRIMARY KEY,
    simile TEXT NOT NULL,
    meaning TEXT NOT NULL
);

CREATE TABLE funny_similes (
    id SERIAL PRIMARY KEY,
    simile TEXT NOT NULL,
    meaning TEXT NOT NULL
);

CREATE TABLE poetic_comparisons (
    id SERIAL PRIMARY KEY,
    comparison TEXT NOT NULL,
    meaning TEXT NOT NULL
);

-- 7. Abbreviations/Prefixes in Common Use
CREATE TABLE internet_texting_abbreviations (
    id SERIAL PRIMARY KEY,
    abbreviation TEXT NOT NULL,
    meaning TEXT NOT NULL
);

CREATE TABLE scientific_medical_prefixes (
    id SERIAL PRIMARY KEY,
    prefix TEXT NOT NULL,
    meaning TEXT NOT NULL
);

CREATE TABLE business_corporate_acronyms (
    id SERIAL PRIMARY KEY,
    acronym TEXT NOT NULL,
    meaning TEXT NOT NULL
);

CREATE TABLE educational_academic_shortforms (
    id SERIAL PRIMARY KEY,
    abbreviation TEXT NOT NULL,
    meaning TEXT NOT NULL
);

CREATE TABLE government_legal_terms (
    id SERIAL PRIMARY KEY,
    term TEXT NOT NULL,
    meaning TEXT NOT NULL
);

-- 8. Some Geographical Facts Worth Remembering
CREATE TABLE world_landmarks (
    id SERIAL PRIMARY KEY,
    landmark TEXT NOT NULL,
    location TEXT NOT NULL,
    fact TEXT NOT NULL
);

CREATE TABLE unique_natural_wonders (
    id SERIAL PRIMARY KEY,
    wonder TEXT NOT NULL,
    location TEXT NOT NULL,
    fact TEXT NOT NULL
);

CREATE TABLE extreme_weather_facts (
    id SERIAL PRIMARY KEY,
    phenomenon TEXT NOT NULL,
    location TEXT,
    fact TEXT NOT NULL
);

CREATE TABLE capital_cities_countries (
    id SERIAL PRIMARY KEY,
    capital_city TEXT NOT NULL,
    country TEXT NOT NULL
);

CREATE TABLE fun_geography_trivia (
    id SERIAL PRIMARY KEY,
    fact TEXT NOT NULL
);

-- 9. Revision Notes in English
CREATE TABLE grammar_essentials (
    id SERIAL PRIMARY KEY,
    topic TEXT NOT NULL,
    explanation TEXT NOT NULL
);

CREATE TABLE literary_devices (
    id SERIAL PRIMARY KEY,
    device TEXT NOT NULL,
    definition TEXT NOT NULL
);

CREATE TABLE common_writing_mistakes (
    id SERIAL PRIMARY KEY,
    mistake TEXT NOT NULL,
    correction TEXT NOT NULL
);

CREATE TABLE exam_tips_tricks (
    id SERIAL PRIMARY KEY,
    tip TEXT NOT NULL
);

CREATE TABLE reading_comprehension_strategies (
    id SERIAL PRIMARY KEY,
    strategy TEXT NOT NULL,
    explanation TEXT NOT NULL
);
