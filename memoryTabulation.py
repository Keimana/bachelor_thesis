import psutil
import memory_profiler
import gc
from tabulate import tabulate
import csv


texts = [
    "100 Most Anticipated books releasing in 2010",
    "10 best films of 2009 - What's on your list?",
    "10 days of free admission at Lan Su Chinese Garden to celebrate their 10th birthday",
    "10 PlayStation games to watch out for in 2010",
    "10 resolutions for a Happy New Year for you and your dachshund",
    "10 Tips to a healthy diet that works",
    "10 tips to avoid the drive-thru and encourage weight loss",
    "10 trends to end in 2010",

]


def memory_decorator(func):
    def wrapper(*args, **kwargs):
        gc.collect()
        
        memory_usages = []
        for _ in range(5):
            initial_memory = memory_profiler.memory_usage()[0]
            result = func(*args, **kwargs)
            final_memory = memory_profiler.memory_usage()[0]
            memory_usage = final_memory - initial_memory
            memory_usages.append(memory_usage)
        
        avg_memory_usage = sum(memory_usages) / len(memory_usages)
        
        return result, avg_memory_usage
    return wrapper


@memory_decorator
def analyze_sentiment(text):
    if "win" in text:
        return "positive"
    elif "free" in text:
        return "neutral"
    elif "pampalaki" in text:
        return "clickbait"
    else:
        return "neutral"

@memory_decorator
def perform_semantic_analysis(text):
    return len(text.split())

@memory_decorator
def perform_syntactic_analysis(text):
    return len(text)

data = []


for text in texts:
    sentiment, memory_sentiment = analyze_sentiment(text)
    
    semantic_result, memory_semantic = perform_semantic_analysis(text)

    syntactic_result, memory_syntactic = perform_syntactic_analysis(text)
    
    data.append([
        text,
        "genuine",
        sentiment,
        semantic_result,
        syntactic_result,
        memory_sentiment,
        memory_semantic,
        memory_syntactic
    ])


headers = [
    "Headline Text",
    "Tag",
    "Sentiment",
    "SSA",
    "SSAM",
    "SSAT",
    "SSA Memory (MB)",
    "SSAM Memory (MB)",
    "SSAT Memory (MB)"
]


print(tabulate(data, headers=headers, tablefmt="fancy_grid"))


def export_to_csv(filename, data, headers):
    with open(filename, mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(headers)  
        writer.writerows(data)  


export_to_csv('memorytabulation.csv', data, headers)
