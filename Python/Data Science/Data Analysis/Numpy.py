import sys
import numpy as np

# basics
np.array([1, 2, 3, 4, 5])
# numpy arrays are accessed in the same way as python lists
# numpy arrays donot modify existing array but instead they create a new array 
a = np.array([1, 2, 3, 4, 5])
a[0]
a[0:]
a[:3]
a[1:4]
a[:]
a[::2]
a[[0, 2, 4]] # multi-indexing allows us to access multiple indexes at once which creates a new numpy array instead of individual elements
# checking for type of an array
a.dtype

# array types
a = np.array([1, 2, 3, 4, 5])
b = np.array([1.3, 2.9, 3.0, 4.5, 5.23])
a.dtype
b.dtype

# creating custom numpy array types
np.array([1, 2, 3, 4, 5], dtype=np.float).dtype
np.array([1, 2, 3, 4, 5], dtype=np.int8).dtype
np.random.randint(10, 100, size=(1, 5)) # 10 is start and 100 is stop. for start 0 you may ignore it and just type the stop

# dimensions and shapes
A = np.array([
    [2, 4, 7],
    [1, 6, 9]
])
# properties of numpy arrays
A.shape
A.ndim # dimensions
A.size
A.sum()
A.mean()
A.std()
A.var()
A.sum(axis=0) # mean of the first axis (2+1, 4+6, 7+9) = (3, 10, 16)
A.mean(axis=1) # mean of the second axis (2+4+7, 1+6+9) = (13, 16)
A[0, 1] # Gives us 4
A[[0, 1]] # Gives us both lists

# modification
A[0] = np.array([4, 5, 6])
A[1] = 4 # assign all with the value 4 (expand operation)

# Broadcasting and vectorized operations
a = np.arange(4) # numpy array of range 4
c = a + 10
b = np.array([10, 20, 30, 40])
b + c

# boolean arrays
a = np.arange(4) 
a[[True, False, False, True]] # returns items at index true
a[a<3] # creates a boolean array which is used to select over the actual array (a)
a[(a>1) & (a<3)] # AND
a[~((a>=1) & (a<3))] # NOT
a[((a==1) | (a==3))] # OR

# return all the even numbers generated from this array
A = np.random.randint(100, size=(3,3))
A
A[A%2==0]

# linear algebra
A = np.random.randint(100, size=(3,3))
B = np.random.randint(100, size=(3,2))
A.dot(B) # multiplying matrices
A@B
A.T
B.T
B.T@A

a = 10
b = np.array([1, 2, 3, 4, 5])

# size of objects in memory
sys.getsizeof(b)
np.dtype(np.int32).itemsize

# performance
a = list(range(1000))
np.arange(1000)

# useful numpy functions
# random
np.random.randint(100, size=(3,3))
np.random.rand() # takes an no of values and creates an array of the given values, empty parameters return one number between 0 and 1
np.random.randn(2, 4) # returns a random sample from the standard normal distribution in the shape 2, 4
np.random.normal(size=(2,2))
np.random.random(size=(4,4))

#arange
np.arange(10)
np.arange(5, 10)
np.arange(0, 1, .2)

# reshape
np.arange(10).reshape(2, 5)
np.arange(10).reshape(5, 2)

# linspace
np.linspace(0, 1, 5)
np.linspace(0, 1, 20)
np.linspace(0, 1, 20, False)
np.linspace(0, 100, 20)
np.linspace(0, 100, 20, False)

# zeros, ones, empty
np.zeros(7,dtype=np.int)
np.zeros((3,4), dtype=np.float)
np.ones(4, dtype=np.int)
np.ones((3,4), dtype=np.int)
np.empty(6, dtype=np.int)
np.empty((3,4), dtype=np.int)

# identity and eye
np.identity(3) # square arrays of the given shape
np.eye(3, 3, k=0) # draws a diagonal on the first row starting from the (k) index towards right. (3, 3) is the shape of the array
np.eye(3, 4, k=3)
np.eye(8, 4, k=1)
np.eye(8, 4, k=-5)
'hello world'[6] # char at index 6

# where
np.where() # where(<condition>, <returned if true>, <returned if false>)
np.where('<condition>')[1] # returns the index of the item where the condition is true in a numpy matrix

np.max('<arraylike> or <list>') # returns the max item from an iterable object
np.min('<arraylike> or <list>') # returns the min item from an iterable object

np.argmax('<arraylike> or <list>') # returns the index of the max value from an iterable object
np.argmin('<arraylike> or <list>') # same case as argmax

np.shape[0] # returns the total number of rows in a numpy matrix
np.shape[1] # returns the total number of columns in a numpy matrix

np.bincount('<array>') # counts the no of instances of each item inside an array of non negative values and returns a list
np.clip('<array>', 0, 1) # where 0 is the minimum value while 1 is the maximum value. array elements are clipped between these extremes.

# concatenate
np.concatenate('N-dimensional array')

# arithmetic
np.prod(iterable) # returns the product of all the numbers in the iterable

np.random.RandomState(1) # set np random state value that can be reproduced

arr1 = np.array([4, 7, 12])
arr2 = np.array([5, 9, 15])
np.concatenate((arr1, arr2)) # merge the content of two or multiple arrays into a single array
np.concatenate((arr1, arr2), axis=1) # merge two NumPy arrays column-wise

# merge nested numpy arrays
arr1 = np.array([[4, 6],[9, 13]])
arr2 = np.array([[8, 3],[12, 19]])
np.concatenate((arr1, arr2), axis=1) 

# Use numpy.stack() Function to Join Arrays along a new axis to form a matrix
arr1 = np.array([5, 9, 15])
arr2 = np.array([4, 7, 12])
np.stack((arr1, arr2))  # stacks the arrays in sequence vertically
np.stack((arr1, arr2), axis=1) # this behaves just like np.concatenate((arr1, arr2), axis=1) but on 2 arrays instead of 2 matrices like concatenate
np.hstack((arr, arr1)) # this behaves just like np.concatenate((arr1, arr2))
np.vstack((arr1, arr2)) # behaves just like np.stack()
np.dstack((arr1, arr2)) # this behaves just like np.stack((arr1, arr2), axis=1)

arr1[np.newaxis, :] # same as array.reshape(1,-1)
arr1[:, np.newaxis] # same as array.reshape(-1,1)

np.expand_dims(arr1, axis=0) # same as array.reshape(1, -1)
np.expand_dims(arr1, axis=1) # same as array.reshape(-1, 1)

np.all() # test whether items in a given axis of an array evaluate to True

np.digitize(data, bins=bins) # bins our data into specified bins, both data and bins are array like
