"""
    This is a module that contains all of the logic and analysis to simulation the research entitled
    ''DESIGNING AN ADAPTIVE PROGRAMMING APPROACH APPLIED IN  CLICKBAIT FILTERING IN SOCIAL MEDIA''
"""

import spacy
from collections import defaultdict

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
  keywords = ["you won't believe", "click here", "shocking truth"]  # Example clickbait keywords
  semantics = []
  for token in doc:
    if token.text.lower() in keywords:
      semantics.append(token.text.lower())
  return semantics

def SSA(text):
  sentiment = get_sentiment(text)
  semantics = get_semantics(text)
  clickbait = False  # Initial assumption, can be modified based on sentiment/semantics

  # Basic clickbait detection logic based on sentiment and semantics (Can be improved)
  if sentiment == "positive" and len(semantics) > 0:
    clickbait = True  # Positive sentiment with clickbait keywords might be clickbait

  return sentiment, semantics, "clickbait" if clickbait else "genuine"

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

    memo_cache[text] = {"sentiment": sentiment, "semantics": semantics, "label": "clickbait" if clickbait else "genuine"}
    return sentiment, semantics, "clickbait" if clickbait else "genuine"

# Tabulation dictionary to store pre-computed classifications (Limited and impractical for real-world use)
tabulation_cache = {
  ("positive", []): "clickbait",  # Example: Positive sentiment with no keywords is classified as clickbait (Needs improvement)
  ("negative", []): "genuine",   # Example: Negative sentiment with no keywords is classified as genuine (Needs improvement)
}

def SSAT(text):
  sentiment = get_sentiment(text)
  semantics = get_semantics(text)
  key = (sentiment, tuple(semantics))  # Combine sentiment with semantics for lookup

  if key in tabulation_cache:
    return sentiment, semantics, tabulation_cache[key]
  else:
    # Default classification (Needs improvement) - Can be modified based on your scenario
    return sentiment, semantics, "unclassified"  # Example: Unseen combinations are marked as unclassified
