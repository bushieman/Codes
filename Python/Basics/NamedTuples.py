from collections import namedtuple

# creating 
point1 = namedtuple("point", 'x y z') # the second argument takes any iterable object
point = point1(1,2,3)
print(point)

# accessing 
print(point.x, point.y, point.z)
print(point[0], point[1], point[2])

# other methods
print(point._asdict())
print(point._fields)
print(point._replace(z=10))
print(point._make(['a', 'b', 'c'])) # assigning
