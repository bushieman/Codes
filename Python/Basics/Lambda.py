# used when there is only one line of expression in our function
# useful for mini functions(functions within functions)

from functools import reduce

func = lambda x,y:x+y
print(func(2,3))

numbers = [1, 2, 3, 4, 5]
points = [(10, 5), (3, 4), (5, 7), (3, 8)]

# map
print(list(map(lambda x: x**2, numbers)))

# filter
print(list(filter(lambda x: x%2!=0, numbers)))

# sorted
print(sorted(numbers, reverse=True))
print(sorted(points, key=lambda x: x[0] + x[1], reverse=True))
print(sorted(list(map(lambda x: x[0] + x[1], points)), reverse=True))

# reduce
print(reduce(lambda x,y: x + y, numbers))

# dataframes
df.Series.apply(lambda x: func(x)) # also df.Series.map(func)
