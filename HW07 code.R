setwd("C:/Users/Wang/source/R/IE522")
df=read.csv("ZMTSLA(2).csv",header=TRUE,fileEncoding="UTF-8-BOM")
#m=nrow(df)
price_zm=df$ZM
x=log(price_zm[2:m]/price_zm[1:(m-1)])
mean_zm=mean(x)
price_tsla=df$TSLA
y=log(price_tsla[2:m]/price_tsla[1:(m-1)])
mean_tsla=mean(y)
D=x-y
n=length(D)
mean_d=mean(D)
mu0=0
se=sd(D)/sqrt(n)
z0=(mean_d-mu0)/se
z0
alpha=0.05
zscore=qnorm(1-alpha/2)
#1 run test
library(randtests)
runs.test(x,alternative="two.sided",threshold=median(x),pvalue="normal",plot=FALSE)
runs.test(D,alternative="two.sided",threshold=median(D),pvalue="normal",plot=FALSE)
#2 shapiro-wilk
shapiro.test(x)
#3
qqnorm(x)
qqline(x)
#4

library(moments)
B=5000
len=length(x)
sample_kurtosis=rep(0,B)
for (b in 1:B){
  xstar=sample(x,len,replace=TRUE)
  sample_kurtosis[b]=kurtosis(xstar)
}


theta_hat=kurtosis(x)
qu_star=quantile(sample_kurtosis,probs=0.975)
ql_star=quantile(sample_kurtosis,probs=0.025)
u=2*theta_hat-qu_star
l=2*theta_hat-ql_star
qu_star
ql_star
u
l
#7
isTRUE(abs(z0)>zscore)
#8
isTRUE(mean(D)<mu0-zscore*se)
ub=mean(D)+zscore*se
ub
#9
p_value=1-pnorm(z0)
p_value
#10

