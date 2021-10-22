getwd()
setwd("C:/Users/Wang/source/R/IE522")
index=read.csv("TSP500.csv",header = TRUE)
n=nrow(index)
m=col(index)
adj<-index$Adj.Close
logreturn<-adj
for(i in 2:n)
{
  logreturn[i-1]<-log(adj[i]/adj[i-1])
}
logreturn[n]<-NA
adjindex<-data.frame(index,logreturn)
adjindex[1:3,]
print(mean(adjindex$logreturn,na.rm=TRUE))
print(sd(adjindex$logreturn,na.rm=TRUE))
print(median(adjindex$logreturn,na.rm=TRUE))
install.packages("moments")
library(moments)
print(skewness(adjindex$logreturn,na.rm=TRUE))
print(kurtosis(adjindex$logreturn,na.rm=TRUE))
print(quantile(adjindex$logreturn,na.rm=TRUE))
logreturn0<-logreturn
for(i in 2:n)
{
  logreturn0[i-1]<-logreturn[i]
}
total_index<-data.frame(adjindex,logreturn0)
total_index[1:3,]
cor(total_index$logreturn,total_index$logreturn0,use="complete.obs")
