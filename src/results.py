import pandas as pd
import networkx
import matplotlib.pyplot as plt
import math

# Read the CSV file into a dataframe
df = pd.read_csv("../data/similarity_results_final.csv")

# Create an undirected graph object
G = networkx.Graph()

#if similarity score is greater than 0.08, add an edge between the two movies. The graph should be undirected. similarity score is the weight of the edge
for index, row in df.iterrows():
    if row['similarity'] > 0.1:
        G.add_edge(row['Title_1'], row['Title_2'], weight=row['similarity'])

# largest connected component
largest_cc = max(networkx.connected_components(G), key=len)

# Create a subgraph object with just the largest connected component
G_final = G.subgraph(largest_cc)

# check if G_final is connected
print(networkx.is_connected(G_final))

# number of nodes & edges in G_final
print("number of nodes: " + str(G_final.number_of_nodes()))
print("number of edges: " + str(G_final.number_of_edges()))

# diameter of G_final
print("diameter: " + str(networkx.diameter(G_final)))

#clustering coefficient of G_final
print("clustering coefficient: " + str(networkx.average_clustering(G_final)))

#degree distribution of G_final
degree_sequence = sorted([d for n, d in G_final.degree()], reverse=True)

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

#apply pagerank algorithm to G_final with alpha = 0.85
pr = networkx.pagerank(G_final, alpha=0.85)

#sort pagerank values in descending order
pr_sorted = sorted(pr.items(), key=lambda x: x[1], reverse=True)

#export pagerank values to csv
pr_df = pd.DataFrame(pr_sorted, columns=['Title', 'pagerank'])
pr_df.to_csv('../data/pagerank_results.csv', index=False)

#estimate p for erdos-renyi graph
p = math.e/((1/2) * G_final.number_of_nodes() * (G_final.number_of_nodes() - 1))

#erdos-renyi graph
G_er = networkx.erdos_renyi_graph(G_final.number_of_nodes(), p)

#clustering coefficient of G_er
print("clustering coefficient: " + str(networkx.average_clustering(G_er)))

#check if clustering coefficient of G_final is greater than G_er
print(networkx.average_clustering(G_final) > networkx.average_clustering(G_er))


#export G_final to edge list with weights as edge attributes
networkx.write_weighted_edgelist(G_final, "../data/edge_list.csv", delimiter=';', encoding='utf-8')

# # create a pyvis network object
# net = Network(height="750px", width="100%", bgcolor="#222222", font_color="white")
#
# # add nodes and edges to the network from the networkx graph
# net.from_nx(G)
#
# #show the network
# net.show("network.html")
