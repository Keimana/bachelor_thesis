"""
    This is a module that contains all of the logic and analysis to simulation the research entitled
    ''DESIGNING AN ADAPTIVE PROGRAMMING APPROACH APPLIED IN  CLICKBAIT FILTERING IN SOCIAL MEDIA''
"""

import spacy
from collections import defaultdict
from tagging import is_clickbait
# Load spaCy model (replace 'en_core_web_sm' with your preferred model)
nlp = spacy.load('en_core_web_sm')

# Function to perform sentiment analysis (positive or negative)
def get_sentiment(text):
    doc = nlp(text)
    sentiment = "neutral"
    for token in doc:
        if token.sentiment == "POS":
            sentiment = "positive"
        elif token.sentiment == "NEG":
            sentiment = "negative"
    return sentiment

# Function to perform basic semantic analysis (keywords) - Can be extended for more complex analysis
def get_semantics(text):
    doc = nlp(text)
    keywords = ["you won't believe", "click here", "shocking truth", "(,", ")"]  # Add more clickbait-related keywords
    semantics = []
    for token in doc:
        if token.text.lower() in keywords:
            semantics.append(token.text.lower())
    return semantics

def SSA(text):
    # Check if the input text is labeled as clickbait in the tagged_post.csv file
    if is_clickbait(text):
        return "negative", [], "clickbait"  # Assume sentiment as negative and label as clickbait
    else:
        return "neutral", [], "genuine"  # Assume sentiment as neutral and label as genuine


# Memoization dictionary to store analyzed text and results
memo_cache = defaultdict(dict)

def SSAM(text):
    if text in memo_cache:
        return memo_cache[text]["sentiment"], memo_cache[text]["semantics"], memo_cache[text]["label"]
    else:
        sentiment = get_sentiment(text)
        semantics = get_semantics(text)
        clickbait = False  # Initial assumption

        # Basic clickbait detection logic based on sentiment and semantics (Can be improved)
        if sentiment == "positive" and len(semantics) > 0:
            clickbait = True  # Positive sentiment with clickbait keywords might be clickbait

        # Modify sentiment and label for clickbait
        if clickbait:
            sentiment = "negative"
            label = "clickbait"
        else:
            label = "genuine"

        memo_cache[text] = {"sentiment": sentiment, "semantics": tuple(semantics), "label": label}
        return sentiment, semantics, label

# Tabulation dictionary to store pre-computed classifications (Limited and impractical for real-world use)
tabulation_cache = defaultdict(dict)

def SSAT(text):
    if text in tabulation_cache:
        return tabulation_cache[text]["sentiment"], tabulation_cache[text]["semantics"], tabulation_cache[text]["label"]
    else:
        sentiment = get_sentiment(text)
        semantics = get_semantics(text)
        clickbait = False  # Initial assumption

        # Basic clickbait detection logic based on sentiment and semantics (Can be improved)
        if sentiment == "positive" and len(semantics) > 0:
            clickbait = True  # Positive sentiment with clickbait keywords might be clickbait

        # Modify sentiment and label for clickbait
        if clickbait:
            sentiment = "negative"
            label = "clickbait"
        else:
            label = "genuine"

        tabulation_cache[text] = {"sentiment": sentiment, "semantics": tuple(semantics), "label": label}
        return sentiment, semantics, label
