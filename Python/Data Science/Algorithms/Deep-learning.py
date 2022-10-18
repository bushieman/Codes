import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

# load data
data = tf.keras.datasets.mnist

# separate training and testing data
(x_train, y_train), (x_test, y_test) = data.load_data()

# normalize our data
x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

# data output
print(x_test)

# create our model
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.softmax))

# compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# train the model
model.fit(x_train, y_train, epochs=3)

# evaluating the model
loss, acc = model.evaluate(x_test, y_test)
print(loss, acc)

# saving a model
model.save('num_predict.model')

# load an existing model
new_model = tf.keras.models.load_model('num_predict.model')

# make predictions
prediction = new_model.predict([x_test])
print(np.argmax(prediction[3]))

# draw the correct result
plt.imshow(x_test[3], cmap=plt.cm.binary)
plt.show()
