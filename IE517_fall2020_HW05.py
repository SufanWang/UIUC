#!/usr/bin/env python
# coding: utf-8

# In[11]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pandas import DataFrame
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from math import sqrt
from sklearn.metrics import r2_score
from sklearn.decomposition import PCA

dt=pd.read_csv("/Users/Wang/source/IE517/hw5/hw5_treasury yield curve data.csv")
dt.head()


# In[3]:


dt=dt.drop('Date',1)
dt.head()


# In[ ]:





# In[34]:


# Plot heatmap of correlation matrix


cm = DataFrame(dt.corr())
hm = sns.heatmap(cm, annot = True, yticklabels= dt.columns, 
                 xticklabels=dt.columns, annot_kws={"size":8})
plt.show()


# In[5]:


cols=['SVENF01','SVENF02','SVENF03','SVENF15','SVENF25','SVENF29','SVENF30','Adj_Close']
sns.pairplot(dt[cols],height=2.5)
plt.tight_layout()
plt.show()


# In[10]:


#Split data into training and test sets

X=dt.iloc[:, :-1].values
y=dt['Adj_Close'].values
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.15,random_state = 42)

#standardize

sc=StandardScaler()
sc.fit(X_train)
X_train_std=sc.transform(X_train)
X_test_std=sc.transform(X_test)


# In[39]:



# Plot heatmap of correlation matrix



cols1 = ['SVENF01','SVENF02', 'SVENF03','SVENF04','SVENF05',
         'SVENF06','SVENF07', 'SVENF08','SVENF09','SVENF10','Adj_Close']
cm = np.corrcoef(dt[cols1].values.T)
hm = sns.heatmap(cm, annot = True, yticklabels=  dt[cols1].columns, 
                 xticklabels=dt[cols1].columns, annot_kws={"size":8})
plt.show()

cols2 = ['SVENF11','SVENF12', 'SVENF13','SVENF14','SVENF15',
         'SVENF16','SVENF17', 'SVENF18','SVENF19','SVENF20','Adj_Close']
cm = np.corrcoef(dt[cols2].values.T)
hm = sns.heatmap(cm, annot = True, yticklabels=  dt[cols2].columns, 
                 xticklabels=dt[cols2].columns, annot_kws={"size":8})
plt.show()

cols3 = ['SVENF21','SVENF22', 'SVENF23','SVENF24','SVENF25',
         'SVENF26','SVENF27', 'SVENF28','SVENF29','SVENF30','Adj_Close']
cm = np.corrcoef(dt[cols3].values.T)
hm = sns.heatmap(cm, annot = True, yticklabels=  dt[cols3].columns, 
                 xticklabels=dt[cols3].columns, annot_kws={"size":8})
plt.show()


# In[ ]:





# In[12]:


#pca
pca=PCA(n_components=None)
X_trian_pca=pca.fit_transform(X_train_std)
X_test_pca=pca.transform(X_test_std)
pca.explained_variance_ratio_


# In[13]:


pca=PCA(n_components=3)


X_train_pca=pca.fit_transform(X_train_std)
X_test_pca=pca.transform(X_test_std)
pca.explained_variance_ratio_





# In[14]:


#cumulative explained variance of the 3 component version
cum_explained_var = []
for i in range(0, len(pca.explained_variance_ratio_)):
    if i == 0:
        cum_explained_var.append(pca.explained_variance_ratio_[i])
    else:
        cum_explained_var.append(pca.explained_variance_ratio_[i] + cum_explained_var[i-1])
print(cum_explained_var)


# In[52]:


import time
start_lrm_org=time.process_time()


#linear regression for original data
lrm_org=LinearRegression()
lrm_org.fit(X_train_std,y_train)

end_lrm_org=time.process_time()

print('time',end_lrm_org-start_lrm_org)

y_train_pred=lrm_org.predict(X_train_std)
y_test_pred=lrm_org.predict(X_test_std)

print(lrm_org.coef_)
#RMSE
print('RMSE train:%.5f,test:%.5f'%(sqrt(mean_squared_error(y_train,y_train_pred)),sqrt(mean_squared_error(y_test,y_test_pred))))
#R2
print('R^2 train:%.5f,test:%.5f'%(r2_score(y_train,y_train_pred),r2_score(y_test,y_test_pred)))


# In[46]:


#linear regression for pca data
start_lrm_org=time.process_time()

lrm_pca=LinearRegression()
lrm_pca.fit(X_train_pca,y_train)

end_lrm_org=time.process_time()

print('time',end_lrm_org-start_lrm_org)

y_train_pred=lrm_pca.predict(X_train_pca)
y_test_pred=lrm_pca.predict(X_test_pca)

#MSE
from sklearn.metrics import mean_squared_error
print('RMSE train:%.5f,test:%.5f'%(sqrt(mean_squared_error(y_train,y_train_pred)),sqrt(mean_squared_error(y_test,y_test_pred))))
#R2
from sklearn.metrics import r2_score
print('R^2 train:%.5f,test:%.5f'%(r2_score(y_train,y_train_pred),r2_score(y_test,y_test_pred)))


# In[48]:


#svm for original data
from sklearn import svm
start_lrm_org=time.process_time()

svm_org=svm.SVR(kernel='poly')
svm_org.fit(X_train_std,y_train)

end_lrm_org=time.process_time()

print('time',end_lrm_org-start_lrm_org)

y_train_pred=svm_org.predict(X_train_std)
y_test_pred=svm_org.predict(X_test_std)
#RMSE
from sklearn.metrics import mean_squared_error
print('RMSE train:%.5f,test:%.5f'%(sqrt(mean_squared_error(y_train,y_train_pred)),sqrt(mean_squared_error(y_test,y_test_pred))))
#R2
from sklearn.metrics import r2_score
print('R^2 train:%.5f,test:%.5f'%(r2_score(y_train,y_train_pred),r2_score(y_test,y_test_pred)))


# In[50]:


#svm for pca data
start_lrm_org=time.process_time()

svm_pca=svm.SVR(kernel='poly')
svm_pca.fit(X_train_pca,y_train)

end_lrm_org=time.process_time()
print(start_lrm_org)
print(end_lrm_org)
print('time',end_lrm_org-start_lrm_org)

y_train_pred=svm_pca.predict(X_train_pca)
y_test_pred=svm_pca.predict(X_test_pca)
#RMSE
from sklearn.metrics import mean_squared_error
print('RMSE train:%.5f,test:%.5f'%(sqrt(mean_squared_error(y_train,y_train_pred)),sqrt(mean_squared_error(y_test,y_test_pred))))
#R2
from sklearn.metrics import r2_score
print('R^2 train:%.5f,test:%.5f'%(r2_score(y_train,y_train_pred),r2_score(y_test,y_test_pred)))


# In[ ]:




