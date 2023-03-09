# Network Analysis
This project involves performing network analysis on several synthetic and real networks. In the first part, we reproduce well-known facts about network models such as Erdos-Renyi, Watts-Strogatz, and Barabasi-Albert. In the second part, we build a movie network and use various network analysis techniques to examine its properties.

## Reproducing Known Network Facts
We generate synthetic networks using the Watts-Strogatz, Erdos-Renyi, and Barabasi-Albert models, and analyze their properties to reproduce well-known facts about these models. We plot the clustering coefficient and average shortest-path as a function of the parameter p in the Watts-Strogatz model, the average shortest-path length as a function of network size in the Erdos-Renyi model, and the degree distribution histogram in a Barabasi-Albert network.

## Analyzing a Movie Network
We build a movie network using the IMDB Dataset, where nodes represent movies, and edges represent similarity between movies. We use various network analysis techniques to examine the properties of this network. We calculate the diameter and transitivity of the network, examine the degree distribution, apply a PageRank algorithm to identify the most important movies, use community detection algorithms to identify communities within the network, and perform additional analyses on these communities.
