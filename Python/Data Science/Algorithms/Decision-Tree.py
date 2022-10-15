import joblib
import pandas as pd
from sklearn import model_selection, tree


# read data
df = pd.read_csv('music.csv')

# label
predict = 'genre'

# sorting data
x = df.drop(columns=[predict]) # also df.drop([predict], 1)
y = df[predict]
x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size=0.2) 

# creating a model
model = tree.DecisionTreeClassifier()

# training the model
model.fit(x_train, y_train)
# store the model after training
joblib.dump(model, 'linearRegression.joblib')

# testing the model
accuracy = model.score(x_test, y_test)
print(accuracy)

# making predictions
predictions = model.predict([[21, 1], [22, 0], [27, 1], [27, 0]])
print(predictions)



