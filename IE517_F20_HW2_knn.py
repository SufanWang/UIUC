import numpy as np
import pandas as pd
from pandas import DataFrame
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier 
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

dt=pd.read_csv("/Users/Wang/source/IE517/hw2/Treasury Squeeze test - DS1.csv")

# Create feature and target arrays
X = dt.iloc[:,2:11]
y = dt.iloc[:,11]

# Split into training and test set
X_train, X_test, y_train, y_test =train_test_split(X, y, test_size = 0.3, random_state=1,stratify=y)

sc=StandardScaler()
sc.fit(X_train)
X_train_std=sc.transform(X_train)
X_test_std=sc.transform(X_test)
k_range=range(1,26)

scores=[]
# Loop over different values of k
for k in k_range:
    # Setup a k-NN Classifier with k neighbors: knn
    knn =  KNeighborsClassifier(n_neighbors=k)

    # Fit the classifier to the training data
    knn.fit(X_train_std,y_train)
    y_pred=knn.predict(X_test_std)
    scores.append(accuracy_score(y_test,y_pred))
   
plt.plot(k_range, scores,color="r",linestyle="-",marker="^",linewidth=1)
plt.xlabel('Number of Neighbors')
plt.ylabel('Accuracy')
plt.show()

print("My name is Sufan Wang")
print("My NetID is: sufanw2")
print("I hereby certify that I have read the University policy on Academic Integrity and that I am not in violation.")
