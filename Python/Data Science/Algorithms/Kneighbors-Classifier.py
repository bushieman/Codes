import joblib
import pandas as pd
from sklearn import model_selection, preprocessing, neighbors


# read data
df = pd.read_csv('car.data')

# sorting irregular data
le = preprocessing.LabelEncoder()
buying = le.fit_transform(list(df['buying']))
maint = le.fit_transform(list(df['maint']))
door = le.fit_transform(list(df['door']))
persons = le.fit_transform(list(df['persons']))
lug_boot = le.fit_transform(list(df['lug_boot']))
safety = le.fit_transform(list(df['safety']))
classf = le.fit_transform(list(df['class']))

x = list(zip(buying, maint, door, persons, lug_boot, safety))
y = list(classf)
x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size=0.2) 

# creating a model
model = neighbors.KNeighborsClassifier(n_neighbors=10)

# training the model
model.fit(x_train, y_train)
# store the model after training
joblib.dump(model, 'linearRegression.joblib')

# testing the model
accuracy = model.score(x_test, y_test)
print(accuracy)

# making predictions
predictions = model.predict(x_test)
for x in range(len(predictions)):
    print("Predictions: ", [predictions[x]], "Data: ", x_test[x], "Actual: ", [y_test[x]])

print("Test set score: {:.2f}".format(np.mean(predictions, y_test)))
