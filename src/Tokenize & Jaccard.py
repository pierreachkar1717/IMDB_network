import pandas as pd
from itertools import combinations
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

def preprocess_text(text):
    # Convert the text to lowercase
    text = text.lower()

    # Tokenize the text
    words = nltk.word_tokenize(text)

    # Remove stop words
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]

    # Stem the words
    stemmer = PorterStemmer()
    words = [stemmer.stem(word) for word in words]

    return words

#jaccard similarity function between two lists
def jaccard_similarity(list1, list2):
    intersection = len(list(set(list1).intersection(list2)))
    union = (len(list1) + len(list2)) - intersection
    return float(intersection / union)

#Data preprocessing
df = pd.read_csv('../data/imdb_top_1000.csv')

#keep only title column and dsescription column
df = df[['Series_Title', 'Overview']]

#remove duplicates inplace
df.drop_duplicates(inplace=True)

#tokenize description with the function above
df['Overview'] = df['Overview'].apply(preprocess_text)


results = []
# Generate all pairs of rows
for row1, row2 in combinations(df.iterrows(), 2):
    # Calculate the Jaccard similarity between the two descriptions
    similarity = jaccard_similarity(row1[1]['Overview'], row2[1]['Overview'])
    # Append the results to the list
    results.append({'Series_Title_1': row1[1]['Series_Title'], 'Series_Title_2': row2[1]['Series_Title'], "similarity": similarity})

# Create a new dataframe from the results list
results_df = pd.DataFrame(results)

# Write the dataframe to a CSV file
results_df.to_csv("../data/similarity_results.csv", index=False)


