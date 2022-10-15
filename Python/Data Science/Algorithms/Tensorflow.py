# nd-array
# GPU support
# Computational graph / Backpropagation
# immutable by default
# mutable by the variable attribute

import os
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# syntax
x = tf.constant(4, shape=(1, 1), dtype=tf.float32)

# rank-1 
x = tf.constant([1, 2, 3])

# rank-2
x = tf.constant([[1, 2, 3], [4, 5, 6]])

# ones
x = tf.ones((3, 3))

# zeros
x = tf.zeros((3, 3))

# eye: the identity matrix
x = tf.eye(3)

# random
x = t                                                                                                         
x = tf.random .uniform((3,3), minval=0, maxval=1)

# range
x = tf.range(10)

# cast
x = tf.range(10)
x = tf.cast(x, dtype=tf.float32)

# elementwise
x = tf.constant([1, 2, 3])
y = tf.constant([4, 5, 6])
# add
z = tf.add(x, y) # also z = x + y
# subtract
z = tf.subtract(x, y) # also z = x - y
# divide
z = tf.divide(x, y) # also z = x / y
# multiply
z = tf.multiply(x, y) # also z = x * y
# dot 
z = tf.tensordot(x, y, axes=1)
# exponential
z = x ** 3
# matrix multiplication
x = tf.random.normal((2, 3))
y = tf.random.normal((3, 5))
z = tf.matmul(x, y) # also z = x @ y note: the column of first element (3) should match the row of the second element (3)

# slicing, indexing
x = tf.constant([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
x[0] # first row
x[0, 1] # first row, second column
x[:, 0] # all rows, first columns
x[0, :] # first row, all columns - same as x[0]
x[0, 1:3] # first row, columns at index 1 and 2

# reshaping
x = tf.random.normal((2, 3))
x = tf.reshape(x, (3, 2)) # can only reshape with similar values 6, 1 is also valid

# numpy
x = tf.random.normal((2, 3))
x = x.numpy() # to numpy
x = tf.convert_to_tensor(x) # to tensor

# strings, lists
x = tf.constant('bushman')
x = tf.constant(['bushman', 'bush', 'bushie', 'bushbaby'])

# variables
x = tf.Variable('bushman')
