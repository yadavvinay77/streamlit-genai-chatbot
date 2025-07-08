import spacy
import re

# Load spaCy model
nlp = spacy.load("en_core_web_sm")


def extract_keywords(text, max_phrases=5):
    """
    Extract top noun chunks and entities as keywords.
    """
    doc = nlp(text)
    # named entities first
    ents = [ent.text for ent in doc.ents]
    # fallback noun chunks
    chunks = [chunk.text for chunk in doc.noun_chunks]
    combined = ents + chunks
    # clean and dedupe
    cleaned = []
    for phrase in combined:
        p = re.sub(r"[^\w\s]", "", phrase).strip()
        if p and p.lower() not in cleaned:
            cleaned.append(p.lower())
    return cleaned[:max_phrases]
