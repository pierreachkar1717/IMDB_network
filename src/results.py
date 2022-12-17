import pandas as pd
import networkx
import matplotlib.pyplot as plt
from pyvis.network import Network

# Read the CSV file into a dataframe
df = pd.read_csv("../data/similarity_results_final.csv")

#list of all movies
movies_1 = df['Series_Title_1'].unique()
movies_2 = df['Series_Title_2'].unique()

#union of both lists
movies = list(set(movies_1) | set(movies_2))

# Create an undirected graph object
G = networkx.Graph()

#if similarity score is greater than 0.08, add an edge between the two movies. The graph should be undirected. similarity score is the weight of the edge
for index, row in df.iterrows():
    if row['similarity'] > 0.08:
        G.add_edge(row['Series_Title_1'], row['Series_Title_2'], weight=row['similarity'])

#largest connected component
largest_cc = max(networkx.connected_components(G), key=len)

# Create a subgraph object with just the largest connected component
G_final = G.subgraph(largest_cc)

#check if Gcc is connected
print(networkx.is_connected(G_final))

#number of nodes & edges in G_final
print("number of nodes: " + str(G_final.number_of_nodes()))
print("number of edges: " + str(G_final.number_of_edges()))

#diameter of G_final
print("diameter: " + str(networkx.diameter(G_final)))

#clustering coefficient of G_final
print("clustering coefficient: " + str(networkx.average_clustering(G_final)))

#degree distribution of G_final
degree_sequence = sorted([d for n, d in G_final.degree()], reverse=True)  # degree sequence

#plot degree distribution as a line graph
plt.plot(degree_sequence)
plt.title("Degree Distribution")
plt.ylabel("Degree")
plt.xlabel("Node")
plt.show()


#plot degree distribution in log scale as a line graph
plt.plot(degree_sequence)
plt.title("Degree Distribution")
plt.ylabel("Degree")
plt.xlabel("Node")
plt.xscale('log')
plt.yscale('log')
plt.show()




#export to edge list
#networkx.write_edgelist(G_final, "../data/edge_list.csv", delimiter=",", data=['weight'])



# # create a pyvis network object
# net = Network(height="750px", width="100%", bgcolor="#222222", font_color="white")
#
# # add nodes and edges to the network from the networkx graph
# net.from_nx(G)
#
# #show the network
# net.show("network.html")
