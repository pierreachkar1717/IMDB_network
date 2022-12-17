import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a dataframe
df = pd.read_csv("../data/similarity_results.csv")

#drop rows with similarity score of 0
df = df[df['similarity'] != 0]

#sort by similarity score
df = df.sort_values(by='similarity', ascending=False)

#drop duplicates where title1 is title2
df = df[df['Series_Title_1'] != df['Series_Title_2']]

#export to csv
df.to_csv('../data/similarity_results_final.csv', index=False)