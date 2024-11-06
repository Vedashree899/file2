1)Select the k no of neighbors
2)Calculate eucledian distance of k no of neighbors from the new data point
3)take the k nearest neighbors as per eucledian distance
4)among these k no of neighbors count the no of data points of each category
5)assign new datapoint to that category for which the count of no of neighbor is maximum
6)get output via model
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df=pd.read_csv(r"C:\Users\
''train-test split'''
from sklearn.neighbors import KNeighborsClassifier
knn_model=KNeighborsClassifier() #n_neighbors=10
knn_model.fit(xtrain,ytrain)
ans=knn_model.predict(xtest)
knn_model.score(xtest,ytest
'confusion matrix'''
SVM(support vector machine) -> SVR(support vector regressor)
#DecisionTreeRegressor
'''from sklearn.tree import DecisionTreeRegressor'''
#RandomForestRegressor
'''from sklearn.ensemble import
