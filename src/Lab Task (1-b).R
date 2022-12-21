library(igraph)

start.time = Sys.time()

smpl<-c(1, 5, 10, 50, 100, 200, 500, 700, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 12000, 15000, 20000, 30000, 40000, 50000, 60000)

#Takes n (number of nodes), epsilon, m (number of iterations) as input and output the average path length of all iterations
Erdos_graph <- function(n, epsilon, m){
  paths <- c()
  p <- ((1+epsilon)*log(n))/n
  for (i in 1:m){
    g <- sample_gnp(n,p)
    paths[i] <- average.path.length(g)# same as mean_distance()
  }
  return(mean(paths))
}

#Experimenting with different nodes number
avg_path <-c()
for(j in 1:length(smpl)){
  avg_path[j] <- Erdos_graph(smpl[j], 1e-2, 3)
}

#replace NaN with 0
avg_path[is.na(avg_path)] <- 0


plot(smpl, avg_path, main = "Lab Task (b)",xlab = "num nodes",ylab = "average shortest path", col="black", type="b")

end.time = Sys.time()
taken.time = end.time - start.time
taken.time

#plot(smpl, avg_len, main = "CSN Lab 1 - Task (b)",xlab = "num nodes",ylab = "average shortest path", col="black", type="b", yaxt = "n", ylim = c(0,5))
#axis(2, at = seq(0,5, by = 1), labels = 0:5)
