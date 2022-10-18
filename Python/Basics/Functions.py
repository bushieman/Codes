# firstname and lastname are parameters
# age is the default argument and must be at the end of the parameters
def names(firstname, lastname, age=21):
    print(f'my name is {firstname} {lastname}')

# bush and man are positional arguments: bush is assigned to the first parameter(firstname) and man to (lastname)
names('bush', 'man')
# keyword arguments: the order is not important
names(lastname='man', firstname='bush')
# for a combination of positional and keyword arguments, positional should always come first
names('bush', lastname='man')
 
# *args and **kwargs
# *args are tuples while **kwargs are dictionaries
def personalInfo(firstname, lastname, *args, **kwargs):
    print(f'Name: {firstname} {lastname}')
    for arg in args:
        print(f'Math Score: {arg}')
    for key in kwargs:
        print(key, kwargs[key])

personalInfo('bush', 'man', 78, 86, 86, 84, 93, age=21, gender='male')

# forced keyword arguments
def foo(a, b, *args, c, d):
    print(a, b, c, d)
    print(f'args, {args}')

foo(1, 2, c=5, d=6)
foo(1, 2, 3, 4, c=5, d=6)

# unpacking arguments
def foo(a, b, c, d):
    print(a, b, c, d)

mylist = [1, 2, 3, 4]
foo(*mylist) 
mydict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
foo(**mydict) 

# local and global varibles
# Local variable: Any variable declared inside a function is known as Local variable and it’s accessibility remains inside that function only.
# Global Variable: Any variable declared outside the function is known as Global variable and it can be easily accessible by any function present throughout the program.

var = 10 # global
def myfunction():
    var = 20 # local
    print(var)

myfunction()
print(var)

# changing global variables
var = 10 
def myfunction():
    global var
    var = 20 

myfunction()
print(var)

# parameter parsing
var = 5
def foo(n):
    n = 10 # this is a local var and has nothing to do with the var; cannot modify var since int are immutable

foo(var)
print(var)

mylist = [1, 2, 3, 4, 5]
def foo(n):
    n.append(6) # lists are mutable; also int inside lists are mutable
    n[0] = 10

foo(mylist)
print(mylist)

mylist = [1, 2, 3, 4, 5]
def foo(n):
    n = [21, 22, 23, 24, 25] # this is local. if we rebind the reference in the method then the outer method will not be changed
    n.append(6) # lists are mutable; also int inside lists are mutable
    n[0] = 10

foo(mylist)
print(mylist)

mylist = [1, 2, 3, 4, 5]
def foo(n):
    n += [21, 22, 23, 24, 25] # this references the global list hence can be appended

foo(mylist)
print(mylist)

mylist = [1, 2, 3, 4, 5]
def foo(n):
    n = n + [21, 22, 23, 24, 25] # this creates a new local list inside the function with mylist values and increases itself with the given values
    print(n)

foo(mylist) 
print(mylist)


# asterisks
# products and powers
product = 5 * 2
power = 5 ** 2
# create lists, tuples or strings with repeated elements
zeros = [0] * 10 
zerone = [0, 1] * 10
zeronetups = (0, 1) * 10
ab = 'AB' * 10
# args and kwargs
def foo(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])

foo(1, 2, 3, 4, 5, 6, age=21, total=4900)
# to enforce keyword arguments
def foo(a, b, *, c):
    print(a, b, c)

foo(1, 2, c=5)
# unpacking lists into functions
def foo(a, b, c):
    print(a, b, c)

mylist = [1, 2, 3]
mytuple = (1, 2, 3)
mydict = {'a': 1, 'b': 2, 'c': 3} # the key should match with the parameters in our function
foo(*mylist)
foo(*mytuple)
foo(*mydict)
foo(**mydict)
# unpacking lists, tuples and sets
numbers = [1, 2, 3, 4, 5]
numbers2 = (1, 2, 3, 4, 5)
*beginning, last = numbers
beginning2, *last2 = numbers2
beginning3, *middle3, last3 = numbers2
beginning4, *middle4, secondlast4, last4 = numbers2
# merging iterables
mylist = [1, 2, 3]
mytuple = (4, 5, 6)
myset = {7, 8, 9}
newlist = [*mylist, *mytuple, *myset]
mydict1 = {'a': 1, 'b': 2, 'c': 3}
mydict2 = {'d': 4, 'e': 5, 'f': 6}
newdict = {**mydict1, **mydict2}
print(newlist)
print(newdict)
