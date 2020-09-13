import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pandas import DataFrame
import numpy as np

dt=pd.read_csv("/Users/Wang/source/IE517/hw3/HY_Universe_corporate bond.csv")

#histogram
sns.set()
_ =plt.hist (dt.loc[:,'Coupon Type'])
_ = plt.xlabel('Coupon Type')
_ = plt.ylabel('count')
plt.title('Histogram of Coupon Type')
plt.show()

#scatter
_ = plt.plot(dt.loc[:,'n_trades'],dt.loc[:,'LiquidityScore'], marker='.', linestyle='none')
_ = plt.xlabel('n_trades')
_ = plt.ylabel('LiquidityScore')
plt.title('scatter plot')
plt.show()

#heatmap
data=dt.iloc[:,21:29]
corMat=DataFrame(data.corr())
plt.pcolor(corMat)
plt.title('heat map')
plt.show

#box
# Create box plot with Seaborn's default settings
_ = sns.boxplot(x='Bloomberg Composite Rating', y='weekly_mean_volume', data=dt)
_ = plt.xlabel('Bloomberg Composite Rating')
_ = plt.ylabel('weekly_mean_volume')
plt.title('box plot')
plt.show()

#qq
from scipy import stats
stats.probplot(dt.loc[:,'weekly_mean_volume'], dist="norm", plot=plt)
plt.title('qq plot of weekly_mean_volume')
plt.show()

print("My name is Sufan Wang")
print("My NetID is:sufanw2")
print("I hereby certify that I have read the University policy on Academic Integrity and that I am not in violation.")