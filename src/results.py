import pandas as pd
import networkx
import matplotlib.pyplot as plt
import math

df = pd.read_csv("../data/similarity_results_final.csv")

G = networkx.Graph()

# construct graph
for index, row in df.iterrows():
    if row['similarity'] > 0.1:
        G.add_edge(row['Title_1'], row['Title_2'], weight=row['similarity'])


# Create a subgraph object with just the largest connected component
largest_cc = max(networkx.connected_components(G), key=len)
G_final = G.subgraph(largest_cc)
print(networkx.is_connected(G_final))


print("number of nodes: " + str(G_final.number_of_nodes()))
print("number of edges: " + str(G_final.number_of_edges()))
print("diameter: " + str(networkx.diameter(G_final)))
print("average shortest path length: " + str(networkx.average_shortest_path_length(G_final)))
print("clustering coefficient: " + str(networkx.average_clustering(G_final)))


degree_sequence = sorted([d for n, d in G_final.degree()], reverse=True)

# plot degree distribution
plt.plot(degree_sequence)
plt.title("Degree Distribution")
plt.ylabel("Degree")
plt.xlabel("Node")
plt.show()


# plot degree distribution in log scale
plt.plot(degree_sequence)
plt.title("Degree Distribution")
plt.ylabel("Degree")
plt.xlabel("Node")
plt.xscale('log')
plt.yscale('log')
plt.show()

# pagerank algorithm with alpha = 0.85
pr = networkx.pagerank(G_final, alpha=0.85)

# visualize the graph with node size proportional to pagerank score
networkx.draw(G_final, node_size=[v * 10000 for v in pr.values()], node_color='orange')
plt.title("IMDB-Dataset")
plt.show()

#sort pagerank values in descending order and export them
pr_sorted = sorted(pr.items(), key=lambda x: x[1], reverse=True)
pr_df = pd.DataFrame(pr_sorted, columns=['Title', 'pagerank'])
pr_df.to_csv('../data/pagerank_results.csv', index=False)

#estimate p for erdos-renyi graph
p = math.e/((1/2) * G_final.number_of_nodes() * (G_final.number_of_nodes() - 1))
G_er = networkx.erdos_renyi_graph(G_final.number_of_nodes(), p)
print("clustering coefficient: " + str(networkx.average_clustering(G_er)))

#check if clustering coefficient of G_final is greater than G_er
print(networkx.average_clustering(G_final) > networkx.average_clustering(G_er))


#export G_final to edge list with weights as edge attributes
networkx.write_weighted_edgelist(G_final, "../data/edge_list.csv", delimiter=';', encoding='utf-8')

