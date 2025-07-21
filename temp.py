import pandas as pd 
import numpy as np 
import seaborn as sns
df=sns.load_dataset("iris")
 
df.head() 
# Dropping the Id column 
#df.drop('Id', axis = 1, inplace = True) 
  
# Renaming the target column into numbers to aid training of the model 
df['species']= df['species'].map({'setosa':0, 'versicolor':1, 'virginica':2}) 
  
# splitting the data into the columns which need to be trained(X) and the target column(y) 
X = df.iloc[:, :-1] 
y = df.iloc[:, -1] 
  
# splitting data into training and testing data with 30 % of data as testing data respectively 
from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0) 
  
# importing the random forest classifier model and training it on the dataset 
from sklearn.ensemble import RandomForestClassifier 
classifier1 = RandomForestClassifier() 
classifier1.fit(X_train, y_train) 
  
# predicting on the test dataset 
y_pred = classifier1.predict(X_test) 
  
# finding out the accuracy 
from sklearn.metrics import accuracy_score 
score = accuracy_score(y_test, y_pred) 
# pickling the model 
import pickle 
pickle_out = open("classifier1.pkl", "wb") 
pickle.dump(classifier1, pickle_out) 
pickle_out.close()
