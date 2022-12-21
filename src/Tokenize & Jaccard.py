import pandas as pd
from itertools import combinations
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

def preprocess_text(text):
    """
    Preprocesses the given text by performing the following operations:
        1. Convert the text to lowercase
        2. Tokenize the text
        3. Remove stop words
        4. Remove punctuations
        5. Stem the words

    Args:
        text (str): The input text to preprocess.

    Returns:
        List[str]: A list of preprocessed words.
    """
    text = text.lower()

    words = nltk.word_tokenize(text)

    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]

    words = [word for word in words if word.isalpha()]

    stemmer = PorterStemmer()
    words = [stemmer.stem(word) for word in words]

    return words

def jaccard_similarity(list1, list2):
    """
    Calculates the Jaccard similarity between two lists.

    The Jaccard similarity is a measure of the overlap between two sets, and is defined as the size of the intersection divided by the size of the union of the sets.

    Args:
    list1 (list): The first list to compare.
    list2 (list): The second list to compare.

    Returns:
    float: The Jaccard similarity between the two lists. """
    intersection = len(list(set(list1).intersection(list2)))
    union = (len(list1) + len(list2)) - intersection
    return float(intersection / union)

#Data preprocessing
df = pd.read_csv('../data/imdb_top_1000.csv')

#combine columns
df['info'] = df['Series_Title'] + ' ' + df['Released_Year'].astype(str) + ' ' + df['Genre'] + ' ' + df['Overview'] + ' ' + df['Director'] + ' ' + df['Star1'] + ' ' + df['Star2'] + ' ' + df['Star3'] + ' ' + df['Star4']

#keep only title and info columns
df = df[['Series_Title', 'info']]

# remove duplicates
df.drop_duplicates(inplace=True)

#apply preprocessing
df['info'] = df['info'].apply(preprocess_text)

#calculate jaccard similarity
results = []
for row1, row2 in combinations(df.iterrows(), 2):
     similarity = jaccard_similarity(row1[1]['info'], row2[1]['info'])
     results.append({'Title_1': row1[1]['Series_Title'], 'Title_2': row2[1]['Series_Title'], "similarity": similarity})

results_df = pd.DataFrame(results)
results_df = results_df.sort_values(by='similarity', ascending=False)

results_df.to_csv("../data/similarity_results.csv", index=False)


