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

    # remove punctuations
    words = [word for word in words if word.isalpha()]

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

#combine series title, release year, genre, overview, directore, star1, star2, star3, star 4 into one column, and name it info
df['info'] = df['Series_Title'] + ' ' + df['Released_Year'].astype(str) + ' ' + df['Genre'] + ' ' + df['Overview'] + ' ' + df['Director'] + ' ' + df['Star1'] + ' ' + df['Star2'] + ' ' + df['Star3'] + ' ' + df['Star4']

# #keep only title and info columns
df = df[['Series_Title', 'info']]

# remove duplicates inplace
df.drop_duplicates(inplace=True)

#tokenize info with the function above
df['info'] = df['info'].apply(preprocess_text)


results = []

# Generate all pairs of rows
for row1, row2 in combinations(df.iterrows(), 2):
     # Calculate the Jaccard similarity between the two info columns
     similarity = jaccard_similarity(row1[1]['info'], row2[1]['info'])
     # Append the results to the list
     results.append({'Title_1': row1[1]['Series_Title'], 'Title_2': row2[1]['Series_Title'], "similarity": similarity})

# Create a new dataframe from the results list
results_df = pd.DataFrame(results)

#sort by similarity score
results_df = results_df.sort_values(by='similarity', ascending=False)

# # Write the dataframe to a CSV file
results_df.to_csv("../data/similarity_results.csv", index=False)


