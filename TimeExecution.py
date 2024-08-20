import time
from functools import wraps

# Define a decorator to measure function execution time
def time_function(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        return result, execution_time
    return wrapper

# Define a memoization cache
memo_cache = {}

# Define a recursive sentiment analysis function
@time_function
def recursive_sentiment_analysis(text):
    # Break down the text into words
    words = text.split()

    # Initialize counters for redundant and new calculations
    redundant_calculations = 0
    new_calculations = 0

    # Function to calculate sentiment for a single word
    def analyze_word(word):
        nonlocal redundant_calculations, new_calculations

        # Check if the word has been analyzed before
        if word in memo_cache:
            # Increment redundant calculation counter and return memoized sentiment
            redundant_calculations += 1
            return memo_cache[word]
        else:
            # Perform sentiment analysis (mock example)
            if len(word) > 4:  # Example condition: words longer than 4 letters are "positive"
                sentiment = "positive"
            else:
                sentiment = "neutral"

            # Store the sentiment in the cache and increment new calculation counter
            memo_cache[word] = sentiment
            new_calculations += 1
            return sentiment

    # Analyze sentiment of each word recursively
    sentiments = [analyze_word(word) for word in words]

    # Return the list of sentiments and counts of redundant and new calculations
    return sentiments, redundant_calculations, new_calculations

# Define example headline texts
texts = [
    "Free Advertising for Small Businesses: Enter to Win a $25,000 Marketing Makeover",
    "How to Win the Lottery - 7 Time Lottery Winner Reveals His Secrets",
    "Vitamins pampalaki ng breast"
]

# Process each headline text
for text in texts:
    # Analyze the text using the recursive function
    (sentiments, redundant_calculations, new_calculations), execution_time = recursive_sentiment_analysis(text)

    # Display the results in a clear, readable format
    print(f"Headline: {text}")
    print(f"Sentiments: {', '.join(sentiments)}")
    print(f"Redundant Calculations: {redundant_calculations}")
    print(f"New Calculations: {new_calculations}")
    print(f"Execution Time: {execution_time:.6f} seconds")
    print()  # Print a blank line for readability between each result
