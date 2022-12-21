library(igraph)


#BA Network with 10000 nodes and 3 edges to add in each time step
ba <- sample_pa(10000, m=3)

#Degree distribution
plot(degree.distribution(ba), xlab = "Degree", ylab = "Frequency", main = "BA-Degree Distribution", lwd = 2)

plot(degree.distribution(ba), xlab = "Degree", ylab = "Frequency", main = "BA-Degree Distribution (Log Scale)", log = 'xy', lwd = 2)
