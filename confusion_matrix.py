# -*- coding: utf-8 -*-
"""confusion matrix.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1G2s1v2I4XxoBy-VOOuvm3L8NDJgCvbQK
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
# %matplotlib inline
df = pd.read_csv('/content/Iris.csv')
df.head()
X = df.drop(['Species'], axis = 1)
y = df['Species']
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X = scaler.fit_transform(X)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, stratify = y, random_state = 0)

classifier = DecisionTreeClassifier(criterion="entropy")
#Applying classifier on training data
classifier = classifier.fit(X_train,y_train)
#make prediction on test data
pred = classifier.predict(X_test)
from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, pred))
#confusion matrix for Decision Tree
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, pred)
print(cm)
df = df.drop(['Species'], axis = 1) 
from six import StringIO  
from IPython.display import Image  
from sklearn.tree import export_graphviz
import pydotplus

from six import StringIO  

dot_data = StringIO()
export_graphviz(classifier, out_file=dot_data, feature_names=df.columns, filled=True, rounded=True,special_characters=True)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
Image(graph.create_png())