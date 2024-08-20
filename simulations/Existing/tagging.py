"""
    This is a script that tags csv files whether it is clickbait or genuine
"""

import re
import spacy
import pandas as pd
import en_core_web_trf

# Load the spaCy English language model
nlp = spacy.load("en_core_web_trf")

nlp = en_core_web_trf.load()

# Read the CSV file
df = pd.read_csv('dataset\clickbait_dataset.csv')

# Create a new column named "tag" to store the classification
df['tag'] = ''

# Helper function to check if a title is clickbait
def is_clickbait(title: str) -> bool:
    """
    Summary:
        A function that marks a given text whether it is clickbait or not

    Args:
        title (str): The given text that will be evaluated

    Returns:
        bool: Returns either true or false
    """
    doc = nlp(title)

    # Check for common clickbait patterns
    if any(token.is_stop for token in doc) and len(doc) < 10:
        return True

    # Check for click-inducing words
    cbait_words = ['you won\'t believe', 'click here', 'shocking truth']  # Add more clickbait keywords
    if any(word.lower() in title.lower() for word in cbait_words):
        return True

    # Check for excessive punctuation
    if len(re.findall(r'[!?]+', title)) > 1:
        return True

    return False

# Iterate Hthrough the rows of the DataFrame and classify the title
for index, row in df.iterrows():
    if is_clickbait(row['headline_text']):
        df.at[index, 'tag'] = 'Clickbait'
    else:
        df.at[index, 'tag'] = 'Genuine'

# Create a new DataFrame with the desired columns
new_df = pd.DataFrame({
    'text_num': [f'post_{i+1}' for i in range(len(df))],
    'headline_text': df['headline_text'],
    'tag': df['tag']
})

# Save the new DataFrame to a new CSV file
new_df.to_csv('tagged_posts.csv', index=False)
