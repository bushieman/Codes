import random, secrets, numpy as np

# random
random.random() # takes atmost 1 argument i.e the no of values to output and returns the numbers each with a value between 0 and 1
random.uniform(10,20) # takes 3 arguments i.e lower-limit=10, upper-limit=20 and size by default is (1,) and returns a float value in that range with the upper limit inclusive
random.randint(10,20) # takes only 2 arguments lower-limit=10 and upper-limit=20 and returns an int value in that range with the upper limit inclusive
# randrange can take 3 arguments: start, stop, step and returns an int value in that range with the upper limit not inclusive. For non loops functions the step is not neccessary
random.randrange(10) # this defaults to start=0, stop=10
random.randrange(10, 20) # start=10, stop=20
random.randrange(10, 20, 2) # start=10, stop=20, step=2 which is not neccessary in this situation
random.randrange(10,20) # custom range integer with upper bound not included
random.normalvariate(0,1) # 0 is the mean and 1 is the standard variation
random.choice(list([1, 2, 3, 4, 5]))
random.choices(list([1, 2, 3, 4, 5]), k=3)
random.sample(list([1, 2, 3, 4, 5]), 2) # can also take a range
random.shuffle([1, 2, 3, 4, 5])
random.seed(5) # reproduce random data
random.randint(10, 20)
random.seed(5)
random.randint(10, 20)



# secrets
secrets.randbelow(10)
secrets.randbits(5) # 5 bits equals to 41 therefore our range will be 0 to 41
random.choice(list([1, 2, 3, 4, 5]))



# numpy
# random.rand function can take any number of parameters and returns floats
np.random.rand(3) # a single item of the shape of 1,3(y,x)
np.random.rand(3,1) # 3 values, each value with the shape of 1,1(y,x)
np.random.rand(3,4) # 3 values, each value has a shape of 1,4(y,x)
np.random.rand(3,4,1) # 3 values, each value has a shape of 4,1(y,x)
np.random.rand(3,4,2) # 3 values, each value with a shape of 4,2(y,x)
np.random.rand(3,4,2,3) # 3 big values, each value has 4 items and each item has the shape of 2,3(y,x)
# basic structure is first 2 values make up the limits other values are stored in a tuple and make up the shapes which are endless
np.random.randint(3) # this defaults to low=0 and high=3
np.random.randint(0,10) #low=0 and high=10
np.random.randint(0,10,3) #low=0 and high=10 and shape of 1,3(y,x)
np.random.randint(0,10,(2,3)) #low=0 and high=10 and two items of the shape of 1,3(y,x)
np.random.randint(0,10,(2,3,1)) #low=0 and high=10 and two items of the shape of 3,1(y,x)
np.random.randint(0,10,(2,2,3,1)) #low=0 and high=10 and two big values each of two items of the shape of 3,1(y,x)
np.random.randn(3,3,2,1)# takes all the functions of the normal np.random.rand but includes negative numbers also
np.concatenate([np.random.randn(10), np.array([10, 15, -10, -15])]) # joins two iterable objects together
np.random.shuffle(np.array([[1,3,5], [4,3,2], [7,4,8]]))
np.random.seed(4) # reproduce random data
np.random.randint(0,10,(3,3))
np.random.seed(4)
np.random.randint(0,10,(3,3))
