#moment method
library(tictoc)
tic()
S10=100
S20=150
r=0.01
q1=0
q2=0.03
sigma1_hat=0.5
sigma2_hat=0.4
t=1
rho=0.1
K=250
z1=rnorm(10000)
z2=rnorm(10000)
z3=rho*z1+sqrt(1-rho^2)*z2

mu1=log(S10)+(r-q1-0.5*sigma1_hat^2)*t
mu2=log(S20)+(r-q2-0.5*sigma2_hat^2)*t
sigma1=sigma1_hat*sqrt(t)
sigma2=sigma2_hat*sqrt(t)
S1t=exp(mu1+sigma1*z1)
S2t=exp(mu2+sigma2*z3)
St=S1t+S2t
a=exp(mu1+0.5*sigma1^2)+exp(mu2+0.5*sigma2^2)
b=exp(2*mu1+2*sigma1^2)+exp(2*mu2+2*sigma2^2)+2*exp(mu1+mu2+0.5*(sigma1^2+sigma2^2+2*rho*sigma1*sigma2))
sigma=sqrt(log(b/a^2))
mu=log(a^2/sqrt(b))
mu
sigma

exp=exp(mu+0.5*sigma^2)
F1=pnorm((mu+sigma^2-log(K))/sigma)
F2=pnorm((mu-log(K))/sigma)
E=exp*F1-K*F2

C = exp(-r*t)*E
toc()
C
#Monte Carlo
Basketoption = function(n,alpha){
  S10=100
  S20=150
  r=0.01
  q1=0
  q2=0.03
  sigma1_hat=0.5
  sigma2_hat=0.4
  t=1
  rho=0.1
  K=250
  mu1=log(S10)+(r-q1-0.5*sigma1_hat^2)*t
  mu2=log(S20)+(r-q2-0.5*sigma2_hat^2)*t
  sigma1=sigma1_hat*sqrt(t)
  sigma2=sigma2_hat*sqrt(t)
  
  if (K-S1t-S2t >0){
    max =K-S1t-S2t
  } else {
    max = 0
  }
  xi =exp(-r*t)*max
  xbar=xi
  ybar=xi^2
  
  for (i in 2:n){
    z1=rnorm(1)
    z2=rnorm(1)
    z3=rho*z1+sqrt(1-rho^2)*z2
    S1t=exp(mu1+sigma1*z1)
    S2t=exp(mu2+sigma2*z3)
    if (K-S1t-S2t >0){
      max = K-S1t-S2t
    } else {
      max = 0
    }
    xi =exp(-r*t)*max
    
    xbar=(1-1/i)*xbar+xi/i
    ybar=(1-1/i)*ybar+(xi^2)/i
  }
  se=sqrt((ybar-xbar^2)/(n-1))
  sd=se*sqrt(n)
  
  m=qnorm(1-alpha/2)
  l=xbar-m*se
  u=xbar+m*se
  output=list("mean"=xbar,"lower bound"=l,"upper bound"=u,"se" = se,"standard deviation" = sd)
  return(output)
}
 result=Basketoption(40960000,0.05) 
result
 