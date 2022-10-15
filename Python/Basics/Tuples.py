# Tuples: ordered, immutable, allow duplicate elements

# creating tuples
mytuple = ('bushman', 21, 'nairobi') # parenthesis are optional
mytuple2 = ('bushie', ) # tuple of one element
mytuple3 = tuple(mytuple)

# iterate over the tuples
for x in mytuple:
    print(x)

# checking for an element in tuple
if "bushman" in mytuple:
    print('yes')

# count
numbers = (1, 2, 4, 3, 2, 4, 5, 4, 7, 8)
numbers.count(4)
numbers.index(2)

# slice
mytuple[::] # [ start: stop: step ]

# reversing lists
mytuple[::-1]

# unpacking
my_tuple = ('bushman', 21, 5.11, True)
name, age, height, is_cool = my_tuple
string, *numbers, boolean = my_tuple # the * assigns all elements between the first(string) and the last(boolean) to the numbers as a list
print(numbers)
