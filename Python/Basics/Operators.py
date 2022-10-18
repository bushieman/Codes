#* Arithmetic operators

a = 10
b = 3

print(a+b) # addition
print(a-b) # subtraction
print(a*b) # multiplication
print(a**b) # a to the power of b
print(a/b) # division float for both int and float values
print(a//b) # division floor for both int and float values
print(-5/2)
print(-5//2) # notice the floor value of a negative number
print(a%b) # modulus

#* Comparison operators i.e evaluates to either True or False
print(a>b) # greater than
print(a<b) # less than
print(a==b) # equal to
print(a!=b) # not equal to
print(a>=b) # greater than or equal to
print(a<=b) # less than or equal to

#* Logical operators: - For combining conditional statements
# And, or, not
# Evaluate to either True or False
# The conditions should also evaluate to either True or False

a = True
b = False

print(a and b) # both should be True
print(a & b) # same as and operator
print(a or b) # atleast one should be True
print(a | b) # same as or operator
print(not b) # should be False
print(~ b) # same as not operator
print(not a and not b) # both should be False

#* Bitwise operators; Act on bits and perform bit-by-bit operations

x = 10
x = 4

print(x&x) # and 
print(x|x) # or
print(~x) # not
print(x^x) # xor
print(x>>x) # right shift
print(x<<x) # left shift

#* Assignment operators; Assigning values to variables


a = 10 # assigning values
b = 5

print(a)
print(b)

a += b # a = a+b
print(a)

a -= b # a = a-b
print(a)

a *= b # a = a*b
print(a)

a /= b # a = a/b
print(a)

a += 2
print(a)

a //= b # a = a//b
print(a)

a *= 12
print(a)

a %= b # a = a//b
print(a)

a **= b # a = a**b
print(a)

a = 2
b = 4

a &= b # a = a&b
print(a)

a |= b # a = a|b
print(a)

a ^= b # a = a^b
print(a)

a >>= b # a = a>>b
print(a)

a <<= b # a = a<<b
print(a)

#* Identity operators
# checks if the values are located on the same part of the memory i.e have the same memory address.
# Two variable that are equal do not imply that they are identical.

x = 10
x = 20
y = x

print(x is not x) # True if the operands are not identical
print(x is y) # True if the operands are identical

#* Membership operators; Test whether value or variable is in a sequence

x = 24 
x = 20
mylist = [10, 20, 30, 40, 50]

if (x not in mylist): # True if value is not found in the sequence
    print("x is NOT present in given list")
else:
    print("x is present in given list")

if (x in mylist): # True if value is found in the sequence
    print("x is present in given list")
else:
    print("x is NOT present in given list")

#* Operator Precedence
# This is used in an expression with more than one operator with different precedence to determine which operation to perform first.
# and takes precedence over or
# multiplication takes precedence over + or -

#* Operator Associativity
# If an expression contains two or more operators with the same precedence, then Operator Associativity is used.
# It can either be Left to Right or from Right to Left.

#> Left‐right associativity
# 100 / 10 * 10 is calculated as
# (100 / 10) * 10 and not
# as 100 / (10 * 10)

# 5 ‐ 2 + 3 is calculated as
# (5 ‐ 2) + 3 and not
# as 5 ‐ (2 + 3)

#> right‐left associativity
# 2 ** 3 ** 2 is calculated as
# 2 ** (3 ** 2) and not
# as (2 ** 3) ** 2

#> “Logical not or !” is meant for boolean values and “bitwise not or ~” is for integers.

#* Ternary operators
a = 5
b = 3
print(a, ' is greater than ', b) if (5>3) else print(a, ' is less than ', b)
print ("Both a and b are equal" if a == b else "a is greater than b"  if a > b else "b is greater than a")


a, b = 10, 20
# Use tuple for selecting an item
# (if_test_false,if_test_true)[test]
# if [a<b] is true it return 1, so element with 1 index will print
# else if [a<b] is false it return 0, so element with 0 index will print
print( (b, a) [a < b] )

# Use Dictionary for selecting an item
# if [a < b] is true then value of True key will print
# else if [a<b] is false then value of False key will print
print({True: a, False: b} [a < b])

# lambda is more efficient than above two methods
# because in lambda we are assure that
# only one expression will be evaluated unlike in tuple and Dictionary
print((lambda: b, lambda: a)[a < b]())

#* Operator overloading

print("Geeks"+" are "+"cool.")
print("Geeks"*5)
 
# we can also overload objects by using their dunder/magic methods
class complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    # adding two objects
    def __add__(self, other):
        return self.a + other.a, self.b + other.b

Ob1 = complex(1, 2)
Ob2 = complex(2, 3)
Ob3 = Ob1 + Ob2
print(Ob3)

class A:
    def __init__(self, a):
        self.a = a
    # greater than comparison
    def __gt__(self, other):
        return "ob1 is greater than ob2" if(self.a>other.a) else "ob2 is greater than ob1"
    # equal to comparison
    def __eq__(self, other):
        return "Both are equal" if (self.a == other.a) else "Not equal"

ob1 = A(2)
ob2 = A(3)
print(ob1>ob2)
print(ob1==ob2)

#> Binary operators
# + __add__(self, other)
# – __sub__(self, other)
# * __mul__(self, other)
# / __truediv__(self, other)
# // __floordiv__(self, other)
# % __mod__(self, other)
# ** __pow__(self, other)
# >> __rshift__(self, other)
# << __lshift__(self, other)
# & __and__(self, other)
# | __or__(self, other)
# ^ __xor__(self, other)

#> Comparison operators
# < __lt__(self, other)
# > __gt__(self, other)
# <= __le__(self, other)
# >= __ge__(self, other)
# == __eq__(self, other)
# != __ne__(self, other)

#> Assignment Operators
# Note: Assigning is not performed incase of immutable containers, such as strings, numbers and tuples.
# A new value has to be assigned containing the results of the operation i.e a variable

# -= __isub__(self, other)
# += __iadd__(self, other)
# *= __imul__(self, other)
# /= __idiv__(self, other)
# //= __ifloordiv__(self, other)
# %= __imod__(self, other)
# **= __ipow__(self, other)
# >>= __irshift__(self, other)
# <<= __ilshift__(self, other)
# &= __iand__(self, other)
# |= __ior__(self, other)
# ^= __ixor__(self, other)

#> Unary Operators
# – __neg__(self)
# + __pos__(self)
# ~ __invert__(self)

#* Any & All
# Any returns True if any of the items is True. It returns False if empty or all are False
print (any([False, False, False, False]))
print (any([False, True, False, False]))
print (any([]))
# All returns True if all of the items are True (or if the iterable is empty) and False if any of the items is False
print (all([True, True, True, True]))
print (all([False, True, True, False]))
print (all([]))
print (all([0])) # note: 0 evaluates to False in Truthy operators and 1-9 return True
print (all([0, 1, 2]))
print (all([1, 2]))

#* Inplace operators
import operator

x = 5
x = 6
a = 5
b = 6

# adding
print(operator.add(a,b)) # normal operator
print(operator.iadd(x,x)) # inplace operator; doesn't change since inplace operations doesnot apply to immutable containers

x = [1, 2, 4, 5]
print(x)
x = operator.add(x,[1, 2, 3])
print(x) # notice x does not change since we are using the normal operator
print(x)
y = operator.iadd(x, [1, 2, 3])
print(x) # notice x had already changed before assigning to y
print(y)

# Some examples are shown below. Basically all the assignment operators can be used here
# operator.imul(a, b) # a *= b -> a = a * b
# operator.itruediv(a, b) # a //= b -> a = a // b
# operator.ifloordiv(a, b) # a /= b -> a = a / b

#* operator functions

a = 5
b=3

print(operator.add(a, b)) # returns the addition of the given arguments i.e a + b
print(operator.sub(a, b)) # returns the difference of the given arguments i.e a - b
print(operator.mul(a, b)) # returns the product of the given arguments i.e a * b
print(operator.truediv(a, b)) # returns the true division of the given arguments i.e a / b
print(operator.floordiv(a, b)) # returns the floor division of the given arguments i.e a // b
print(operator.pow(a, b)) # returns the exponential of the given arguments i.e a ** b
print(operator.mod(a, b)) # returns the modulus of the given arguments i.e a % b
print(operator.lt(a, b)) # checks if a is less than b or not i.e a < b
print(operator.le(a, b)) # checks if a is less than or equal to b or not i.e a <= b
print(operator.eq(a, b)) # checks if a is equal to b or not i.e a == b
print(operator.gt(a, b)) # checks if a is greater than b or not i.e a > b
print(operator.ge(a, b)) # checks if a is greater than or equal to b or not i.e a >= b
print(operator.ne(a, b)) # checks if a is not equal to b or not i.e a != b

x = "geeks"
y = "forgeeks"
# using iconcat() to concat the sequences
z = operator.iconcat(x, y) # concatenates string y at end of string x 
print(z)

#* a += b is not always a = a + b
# whenever we create or modify int, float, char, string they create new
# objects and assign their newly created reference to their respective
 # variables but the same behavior is not seen in the list
a = 10
b = a # points to 1st A object
a = a + 10
c = a # points to 2nd A object
a += 10 # 3rd A object

print(a)
print(b)
print(c)

list1 = [5, 4, 3, 2, 1]
list2 = list1
list1 += [1, 2, 3, 4] # modifying value in current reference
print(list1) # expected results are [5, 4, 3, 2, 1, 1, 2, 3, 4]
print(list2) # expected results are [5, 4, 3, 2, 1, 1, 2, 3, 4]

list1 = [5, 4, 3, 2, 1]
list2 = list1
list1 = list1 + [1, 2, 3, 4]
print(list1) # expected results are [5, 4, 3, 2, 1, 1, 2, 3, 4]
print(list2) # expected results are [5, 4, 3, 2, 1]

# expression list1 += [1, 2, 3, 4] modifes the list in-place, which means it extends the list such that “list1” and “list2” still have the reference to the same list.
# expression list1 = list1 + [1, 2, 3, 4] creates a new list and changes “list1” reference to that new list and “list2” still refer to the old list.

#* Membership Operators:- used to validate the membership of a value in a sequence, such as strings, lists or tuples.

name, age, defaulters = 'Bushman', 21, ['monica', 'rachel', 'amanda', 'clark']

# in operator
print(f'{name} can have a drink with Kimmi') if (age in range(18, 120)) else print(f'{name} is still a baby')

# not in operator
print(f'{name} is eligible for a loan') if (name.lower() not in defaulters) else print(f'{name} is not eligible for a loan')

#* Identity operators:-  usded to determine whether a value is of a certain class or type. They are usdually used to determine the type of data a certain variable contains.
# is operator
x = 5
print("true") if (type(x) is int) else print("false")

# is not operator
print("true") if (type(x) is not str) else print("false")
