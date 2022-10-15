# Lists: ordered, mutable, allow duplicate elements

# creating lists
mylist1 = ['banana', 'cherry', 'apples', 'oranges']
mylist2 = list(np.array) # this method is redundant
mylist3 = ['a'] * 5 # creating 5 similar elements

# iterate over the list
for x in mylist1:
    print(x)

# modify
mylist1[0] = "pineapples"
mylist1[2:2] = 'a' # could not solve it with a string

# copy of a list
mylist1_copy = mylist1 # Note: modification to this list will also modify the original
mylist1_copy = mylist1.copy()
mylist1_copy = list(mylist1)
mylist1_copy = mylist1[:]

# checking for an element in list
if "banana" in mylist1:
    print('yes')

# append and extend
name = 'bushman'
age = 21
mylist1.append() # takes an item
mylist1.extend() # extend the list by elements from iterables
mylist1.extend(name) # valid since string is iterable
mylist1.extend(age) # invalid since int is not iterable
mylist1.extend([age]) # valid since we created a list containing the int

# list comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sqr = [ i**2 for i in numbers]
sqr_of_even = [ i**2 for i in numbers if i%2==0]
print(sqr)
print(sqr_of_even)

# adding lists
mylist3 = mylist1 + mylist2

# inserting 
mylist1.append('blueberries') # end of the list
mylist1.insert(2, 'avocado') # specific position

# removing 
mylist1.pop() # last item
mylist1.remove('avocado') # specified item

mylist2.clearing()
mylist1.reverse()
reversed(mylist1)

# sorting 
mylist1.sort() # will modify the original list
newlist = sorted(mylist1, reverse=False) # sort without modifying original list. You can also provide the reverse parameter to reverse the order; default False.

# slice
mylist1[::] # [ start: stop: step ]

# reversing lists
mylist1[::-1]

mynumlist = ['1', '2', '3', '4', '5'] # must take str items
print(' < '.join(mynumlist))

fruits = ['oranges', 'grapes', 'bananas', 'apples', 'pineapples']
for x, y in enumerate(fruits, start=1): # keeps track of the list item and its index in a for loop
    # if you don’t want to start your count at 0, just use the optional start parameter to set an offset; default=0
    print(x, y)

# indexing
numbers = [1, 2, 3, 4, 5]
numbers.index(3) # returns the index of 3 in the list 

np.argmax([1,2,3,4,5]) # returns the index of the max value in the list i.e 4
np.argmin([1,2,3,4,5]) # returns the index of the min value in the list i.e 0

[1,2,3,4,5].index(max([1,2,3,4,5])) # returns the index of the max value in the list i.e 4
[1,2,3,4,5].index(min([1,2,3,4,5])) # returns the index of the min value in the list i.e 0

import operator

max(enumerate([1,2,3,4,5]), key=operator.itemgetter(1)) # returns (max_key, max_value)
min(enumerate([1,2,3,4,5]), key=operator.itemgetter(1)) # returns (min_key, min_value)
