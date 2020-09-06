from sklearn.tree import DecisionTreeClassifier
import numpy as np
import pandas as pd
from pandas import DataFrame
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

dt=pd.read_csv("/Users/Wang/source/IE517/hw2/Treasury Squeeze test - DS1.csv")
X = dt.iloc[:,2:11]
y = dt.iloc[:,11]
dt = DecisionTreeClassifier(criterion='entropy',max_depth=6, random_state=1)
X_train, X_test, y_train, y_test =train_test_split(X, y, test_size = 0.3, random_state=1,stratify=y)

sc=StandardScaler()
sc.fit(X_train)
X_train_std=sc.transform(X_train)
X_test_std=sc.transform(X_test)
# Fit dt to the training set
dt.fit(X_train_std,y_train)

# Predict test set labels
y_pred = dt.predict(X_test_std)
print(y_pred[0:5])


# Compute test set accuracy  
acc = accuracy_score(y_test, y_pred)
print("Test set accuracy: {:.2f}".format(acc))

print("My name is Sufan Wang")
print("My NetID is: sufanw2")
print("I hereby certify that I have read the University policy on Academic Integrity and that I am not in violation.")




