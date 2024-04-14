from tabulate import tabulate
import csv
texts = [
    "Top 100 Biggest Cinema Hits of 2021",
    "Top 100 Best Tourist Spots in Italy",
    "Top 100 Actresses in the World",
    "2021 Most Influential People",
    "5 Tips for a Healthy Lifestyle",
    "The Future of Technology",
    "Climate Change: Challenges and Opportunities",
]

def classify_headline(text):
    if any(phrase in text.lower() for phrase in ["top 10", "top 100", "biggest", "best", "secrets", "you won't believe", "shocking", "mind-blowing"]):
        return "clickbait"
    else:
        return "genuine"

def analyze_sentiment(text):
    if any(word in text.lower() for word in ["great", "best", "excellent"]):
        return "positive"
    elif any(word in text.lower() for word in ["bad", "worst", "terrible"]):
        return "negative"
    else:
        return "neutral"

def perform_semantic_analysis(text):
    return len(text.split())

def perform_syntactic_analysis(text):
    return len(text)


data = []

for text in texts:
    tag = classify_headline(text)
    
    sentiment = analyze_sentiment(text)
    
    semantic_result = perform_semantic_analysis(text)
    syntactic_result = perform_syntactic_analysis(text)

    data.append([
        text,
        tag,
        sentiment,
        semantic_result,
        syntactic_result
    ])


headers = [
    "Headline Text",
    "Tag",
    "Sentiment",
    "SSA",  # Semantic Analysis (word count)
    "SSAT"  # Syntactic Analysis (character count)
]


print(tabulate(data, headers=headers, tablefmt="fancy_grid"))


def export_to_csv(filename, data, headers):
    with open(filename, mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(headers)  
        writer.writerows(data)  

export_to_csv('limitedadaptability.csv', data, headers)