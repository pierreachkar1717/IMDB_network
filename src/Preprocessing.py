import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/similarity_results.csv")

#drop rows with similarity score of 0
df = df[df['similarity'] != 0]

#sort by similarity score
df = df.sort_values(by='similarity', ascending=False)

#drop rows if they contain the same movie
df = df[df['Title_1'] != df['Title_2']]

#plot the similarity score distribution
plt.hist(df['similarity'], bins=100)
plt.title("Similarity Score Distribution")
plt.ylabel("Frequency")
plt.xlabel("Similarity Score")
plt.show()


df.to_csv('../data/similarity_results_final.csv', index=False)