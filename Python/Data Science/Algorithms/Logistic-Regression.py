from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import missingno as msno
import math

# load data
train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

# clean data
train.drop('Cabin', axis=1, inplace=True)
train.dropna(inplace=True)

# create discrete data
pclass = pd.get_dummies(train['Pclass'], drop_first=True) # drop_first keeps the new binned data and drops the original
sex = pd.get_dummies(train['Sex'], drop_first=True)
embarked = pd.get_dummies(train['Embarked'], drop_first=True)

# load discrete data into df
train = pd.concat([train, sex, pclass, embarked], axis=1) 

# more data wrangling
train.rename(columns={'male': 'Gender', 2: 'Second_class', 3: 'Third_class'}, inplace=True)
train.drop(['Pclass', 'Sex', 'Embarked', 'PassengerId', 'Name', 'Ticket'], axis=1, inplace=True)

# train and test data
X=train.drop('Survived', axis=1)
y = train['Survived']

# split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=100) # random_state creates random datasets for the given value

# create a model
model = LogisticRegression()

# fit
model.fit(X_train, y_train)

# predictions
predictions = model.predict(X_test)

# classification report
classification_report(y_test, predictions)

# confusion matrix
confusion_matrix(y_test, predictions)

# accuracy score
accuracy_score(y_test, predictions)

# standard scaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
