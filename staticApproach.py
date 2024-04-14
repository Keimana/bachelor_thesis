from tabulate import tabulate
import csv

# Sample snippet dataset 
texts = [
    "100 Most Anticipated books releasing in 2010",
    "10 best films of 2009 - What's on your list?",
    "10 days of free admission at Lan Su Chinese Garden to celebrate their 10th birthday",
    "10 PlayStation games to watch out for in 2010",
    "10 resolutions for a Happy New Year for you and your dachshund",
    "10 Tips to a healthy diet that works",
    "10 tips to avoid the drive-thru and encourage weight loss",
    "10 trends to end in 2010",
    "11 year-old girl and 15 year-old boy accused of attempting to kill mother: Who is the adult?",
    "12 Days of Rotoff: Vijay Singh",
    "12 New Year's resolutions for better eating",
    "14 Hours of Energy Conference",
    "Entertainment farewells",
    "In Review: Lacrosse inches into the mainstream",
    "Review: Climategate to Copenhagen Part I"
]

def determine_semantic_meaning(text):
    if "most anticipated" in text or "top 100" in text:
        return "Similar to a Known Title"
    elif "days of" in text or "hours of" in text:
        return "Entice Users"
    elif "trends" in text or "resolutions" in text:
        return "Misleading Title"
    elif "tips" in text:
        return "Attention Seeking"
    elif "kill" in text or "accused" in text:
        return "Deceptive Sentiment"
    else:
        return "Genuine Post"

def analyze_sentiment(text):
    if "kill" in text or "accused" in text:
        return "negative"
    elif "free" in text:
        return "positive"
    else:
        return "neutral"

def classify_tag(text):
    if "most anticipated" in text or "tips" in text or "trends" in text:
        return "clickbait"
    else:
        return "genuine"

data = []

for text in texts:
    tag = classify_tag(text)

    sentiment = analyze_sentiment(text)

    semantic_meaning = determine_semantic_meaning(text)

    # For the purpose of this,  assume SSA, SSAM, SSAT are calculated based on the functions. (1)
    # In practice, these functions would be defined similarly to perform different analyses. (2)
    SSA = len(text.split())  # Number of words as a simple SSA measure (3)
    SSAM = len(set(text.split()))  # Number of unique words as a simple SSAM measure (4)
    SSAT = len(text)  # Number of characters as a simple SSAT measure (5)


    data.append([
        text,
        tag,
        sentiment,
        semantic_meaning,
        SSA,
        SSAM,
        SSAT
    ])


headers = [
    "Headline Text",
    "Tag",
    "Sentiment",
    "Semantic Meaning",
    "SSA",
    "SSAM",
    "SSAT"
]

print(tabulate(data, headers=headers, tablefmt="fancy_grid"))

def export_to_csv(filename, data, headers):
    with open(filename, mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(headers)  
        writer.writerows(data)  

export_to_csv('staticapproach.csv', data, headers)