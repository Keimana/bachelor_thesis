import time
from functools import wraps

def time_function(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        return result, execution_time
    return wrapper

memo_cache = {}

@time_function
def recursive_sentiment_analysis(text):
    words = text.split()

    redundant_calculations = 0
    new_calculations = 0

    def analyze_word(word):
        nonlocal redundant_calculations, new_calculations

        if word in memo_cache:
            redundant_calculations += 1
            return memo_cache[word]
        else:
            if len(word) > 4: 
                sentiment = "positive"
            else:
                sentiment = "neutral"

            memo_cache[word] = sentiment
            new_calculations += 1
            return sentiment

    sentiments = [analyze_word(word) for word in words]

    return sentiments, redundant_calculations, new_calculations

texts = [
    "Free Advertising for Small Businesses: Enter to Win a $25,000 Marketing Makeover",
    "How to Win the Lottery - 7 Time Lottery Winner Reveals His Secrets",
    "Vitamins pampalaki ng breast"
]
for text in texts:
    (sentiments, redundant_calculations, new_calculations), execution_time = recursive_sentiment_analysis(text)

    print(f"Headline: {text}")
    print(f"Sentiments: {', '.join(sentiments)}")
    print(f"Redundant Calculations: {redundant_calculations}")
    print(f"New Calculations: {new_calculations}")
    print(f"Execution Time: {execution_time:.6f} seconds")
    print()  
