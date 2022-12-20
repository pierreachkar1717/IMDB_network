import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a dataframe
df = pd.read_csv("../data/similarity_results.csv")

#drop rows with similarity score of 0
df = df[df['similarity'] != 0]

#sort by similarity score
df = df.sort_values(by='similarity', ascending=False)

#drop duplicates where title1 is title2
df = df[df['Title_1'] != df['Title_2']]


#plot the similarity score distribution
plt.hist(df['similarity'], bins=100)
plt.title("Similarity Score Distribution")
plt.ylabel("Frequency")
plt.xlabel("Similarity Score")
plt.show()

#export to csv
df.to_csv('../data/similarity_results_final.csv', index=False)