from sklearn import datasets, svm, model_selection, metrics

cancer = datasets.load_breast_cancer()

x = cancer.data
y = cancer.target

x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size=0.2)

clf = svm.SVC(kernel="linear", C=2) # C is the soft margin
clf.fit(x_train, y_train)
prediction  = clf.predict(x_test)
accuracy = metrics.accuracy_score(y_test, prediction)
print(accuracy)
