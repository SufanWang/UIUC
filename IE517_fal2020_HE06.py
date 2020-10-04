#!/usr/bin/env python
# coding: utf-8

# In[33]:


import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import StratifiedKFold
import numpy as np
from sklearn.model_selection import cross_val_score

dt=pd.read_csv("/Users/Wang/source/IE517/hw6/ccdefault.csv")
# Create feature and target arrays
X = dt.iloc[:,2:24]
y = dt[['DEFAULT']]
acc_train_list=[]
acc_test_list=[]
#part1
steps = [('scaler',StandardScaler()),
        ('dicisiontree', DecisionTreeClassifier(random_state=1))]
pipeline_1 = Pipeline(steps)

for i in range(1,11):
    X_train, X_test, y_train, y_test =train_test_split(X, y, test_size = 0.1, stratify=y,random_state=i)
    pipeline_1.fit(X_train,y_train)
    y_test_pred = pipeline_1.predict(X_test)
    y_train_pred= pipeline_1.predict(X_train)
    acc_train=accuracy_score(y_train, y_train_pred)
    acc_test = accuracy_score(y_test, y_test_pred)
    
    acc_train_list.append(acc_train)
    acc_test_list.append(acc_test)
    print('Accuracy train: %.5f, Accuracy test: %.5f' %(acc_train,acc_test))


# In[35]:


acc_train_mean=np.mean(acc_train_list)
acc_test_mean=np.mean(acc_test_list)
acc_train_std=np.std(acc_train_list)
acc_test_std=np.std(acc_test_list)
print('Mean of the accuracy of training dataset: %.5f'%(acc_train_mean))
print('Mean of the accuracy of test dataset: %.5f'%(acc_test_mean))
print('standard deviation of the accuracy of training dataset: %.5f'%(acc_train_std))
print('standard deviation of the accuracy of test dataset: %.5f'%(acc_test_std))


# In[36]:


tree= DecisionTreeClassifier(random_state=1)
cv_scores =cross_val_score(tree, X_test, y_test, cv=10)
print('Mean of the accuracy of test dataset: %.5f'%(np.mean(cv_scores)))
print('standard deviation of the accuracy of test dataset: %.5f'%(np.std(cv_scores)))
print(cv_scores)

tree= DecisionTreeClassifier(random_state=1)
cv_scores =cross_val_score(tree, X_train, y_train, cv=10)
print('Mean of the accuracy of training dataset: %.5f'%(np.mean(cv_scores)))
print('standard deviation of the accuracy of training dataset: %.5f'%(np.std(cv_scores)))
print(cv_scores)


# In[ ]:




