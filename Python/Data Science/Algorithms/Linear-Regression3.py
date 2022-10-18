import joblib
import numpy as np
import pandas as pd
from sklearn import model_selection, linear_model

# read data
df = pd.read_csv('student-mat.csv', sep=';')
df = df[['age', 'absences', 'G1', 'G2', 'G3']] # picking specific columns from the csv file

# label
predict = 'G3'

# sorting data
x = np.array(df.drop(columns=[predict])) # also df.drop([predict], 1)
y = np.array(df[predict])
x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size=0.2) 

# creating a model
model = linear_model.LinearRegression()

# training the model
model.fit(x_train, y_train)
# store the model after training

joblib.dump(model, 'linearRegression.joblib')

# load the model
linear = joblib.load('linearRegression.joblib')

# testing the model
accuracy = model.score(x_test, y_test)
print(accuracy)

# making predictions
predictions = model.predict(x_test)
for x in range(len(predictions)):
    print("Predictions: ", [predictions[x]], "Data: ", x_test[x], "Actual: ", [y_test[x]])

# one time training
# best = 0
# for _ in range(50):
#     x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size=0.2) 
#     linear = linear_model.LinearRegression()
#     linear.fit(x_train, y_train)
#     accuracy = linear.score(x_test, y_test)
#     if (accuracy > best):
#         best = accuracy
#         joblib.dump(linear, 'linearRegression.joblib')

    
