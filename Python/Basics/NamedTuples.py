# Like dictionaries, they contain keys that are hashed to a particular value. But on contrary, it supports both access from key-value and iteration, the functionality that dictionaries lack.

from collections import namedtuple

# creating 
point1 = namedtuple("point", 'x y z') # the second argument takes any iterable object
point = point1(1,2,3)
print(point)

# accessing 
print(point.x, point.y, point.z) # using name
print(point[0], point[1], point[2]) # using index
print(getattr(point, 'z')) # using getattr()

# conversion
mylist = [4, 5, 6]
di = {'x': 7, 'y': 8, 'z': 9}
  
print(point._make(li)) # return namedtuple()
print(point._asdict()) # return OrderedDict()
  
print(point(**di))# ** operator returns namedtuple from dictionary

# other methods
print(point._asdict())
print(point._fields) # get all the keynames
print(point._replace(z=10)) # returns a new namedtuple ie doesnot modify original
print(point._make(['a', 'b', 'c'])) # assigning
