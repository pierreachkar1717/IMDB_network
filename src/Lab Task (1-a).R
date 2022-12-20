library(igraph)
library(caret)

start.time = Sys.time()
p <- 10^(seq(-4,-0,0.2)) # sequence with e-4, e-3.8, e-3.6, ...

#Watts-Strogatz small-world model, a function that returns the average of shortest
# distance and clustering coefficient as a list after 20 iterations
Wa_Graph <- function(n, i){
  av_p <- c()
  co <- c()
  for (j in 1:20){ 
    g <- sample_smallworld(dim=1,size=n, nei=4, i)
    av_p[j] <- average.path.length(g)
    co[j] <- transitivity(g)
  }
  av_p_avg <- mean(av_p)
  co_avg <- mean(co)
  
  return(list(av_p_avg, co_avg))
}

#Iterating over p values for the average shortest path & clustering coefficient
avg_s_p_l <- c() 
clustering_coeffs_l<- c() 
for(i in p){
  x <- Wa_Graph(1000, i)
  avg_s_p_l <- c(avg_s_p_l, x[1])
  clustering_coeffs_l <- c(clustering_coeffs_l, x[2])
}

#Convert lists to vector
avg_s_p <-unlist(avg_s_p_l)
clustering_coeffs <-unlist(clustering_coeffs_l)


#Normalize them
avg_s_p <- avg_s_p/avg_s_p[1]
clustering_coeffs <- clustering_coeffs/clustering_coeffs[1]

avg_s_p
clustering_coeffs

plot(p, avg_s_p, ylim=c(0,1), main = "Lab Task (a)",xlab = "p",ylab = " ", col="black", log="x", pch=16)
points(p, clustering_coeffs, ylim=c(0,1), ylab = " ", col="black", pch=0)
text(x=0.001, y=0.2, "L(p) / L(0)")
text(x=0.01, y=0.8, "C(p) / C(0)")

#Plotting Logarithmic Scale 
log10Tck <- function(side, type){
  lim <- switch(side, 
                x = par('usr')[1:2],
                y = par('usr')[3:4],
                stop("side argument must be 'x' or 'y'"))
  at <- floor(lim[1]) : ceiling(lim[2])
  return(switch(type, 
                minor = outer(1:9, 10^(min(at):max(at))),
                major = 10^at,
                stop("type argument must be 'major' or 'minor'")
  ))
}

axis(1, at=log10Tck('x','major'), tcl= 0.2) # bottom
axis(3, at=log10Tck('x','major'), tcl= 0.2, labels=NA) # top
axis(1, at=log10Tck('x','minor'), tcl= 0.1, labels=NA) # bottom
axis(3, at=log10Tck('x','minor'), tcl= 0.1, labels=NA) # top
axis(2) # normal y axis
axis(4) # normal y axis on right side of plot
box()


end.time = Sys.time()
taken.time = end.time - start.time
taken.time

