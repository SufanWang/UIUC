import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pandas import DataFrame
import numpy as np
from scipy import stats

dt=pd.read_csv("/Users/Wang/source/IE517/hw3/HY_Universe_corporate bond.csv")

#histogram
sns.set()
_ =plt.hist (dt.loc[:,'LiquidityScore'],bins=20)
_ = plt.xlabel('LiquidityScore')
_ = plt.ylabel('count')
plt.show()

#scatter
_ = plt.plot(dt.loc[:,'Client_Trade_Percentage'],dt.loc[:,'LiquidityScore'], marker='.', linestyle='none')
_ = plt.xlabel('Client_Trade_Percentage')
_ = plt.ylabel('LiquidityScore')
plt.show()

#heatmap
data=dt.iloc[:,21:29]
corMat=DataFrame(data.corr())
plt.pcolor(corMat)
plt.show

#box
# Create box plot with Seaborn's default settings
_ = sns.boxplot(x='Bloomberg Composite Rating', y='weekly_mean_volume', data=dt)
_ = plt.xlabel('Bloomberg Composite Rating')
_ = plt.ylabel('weekly_mean_volume')
plt.show()

#qq

stats.probplot(dt.loc[:,'weekly_mean_volume'], dist="norm", plot=plt)
plt.show()

print("My name is Sufan Wang")
print("My NetID is:sufanw2")
print("I hereby certify that I have read the University policy on Academic Integrity and that I am not in violation.")
