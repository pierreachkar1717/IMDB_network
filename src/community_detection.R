library(igraph)
library(clustAnalytics)

setwd("~/Downloads/IRRS_05/data")


#Load edgelist as DataFrame
edgelist  <- read.csv("edge_list.csv", sep= ";")

#Read edgelist from Dataframe
g <- graph_from_data_frame(edgelist, directed = FALSE)

#Plot the network
plot(g, vertex.label=NA, vertex.size=6, edge.width=5, layout=layout.fruchterman.reingold, main="IMDB-Dataset")

eva <- evaluate_significance(g, alg_list = list (EdgeBetweenes = cluster_edge_betweenness,
                                                        Fastgreedy = cluster_fast_greedy,
                                                        LableProp = cluster_label_prop,
                                                        Louvain= cluster_louvain, 
                                                        Walktrap = cluster_walktrap))
#Louvin is the one with the highest Modularity
lp <- multilevel.community(g)

#Extract Communities
sizes(lp)
membership <- membership(lp)
mem_name <- lp$names
mem_clust <- lp$membership
members_df<- data.frame(mem_name, mem_clust)
members_df<- members_df[order(members_df$mem_clust), ]

write.csv(members_df, "~/Downloads/IRRS_05/data/communities.csv", row.names=FALSE)

#Barplot of communties sitzes
barplot(sizes(lp), xlab="Community", ylab = "Number of Members", col = "Dark Blue")

#Plot the communities
plot(g, vertex.size = 6, vertex.label=NA, vertex.color=membership(lp), layout=layout.fruchterman.reingold, main="IMDB-Dataset-Communities")


