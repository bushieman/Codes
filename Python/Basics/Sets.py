# sets are unordered, mutable and have no duplicates
# you can create a set with an iterable object
# dictionaries with unique items

# sets store elements in a manner that allows near ­constant ­time checks whether a value is in the set or not, unlike lists, which require linear­time lookups.
# The difference in lookup time means that the time complexity for adding to a set grows at a rate of O(N), which is much better than the O(N²) from lists.

myset1 = {1,2,3,4,5}
myset2 = set({2, 'bushman', 5.4, True})
emp_set = set() # empty set
frozen = frozenset(myset1) # creates an immutable set

# iterate over the set
for x in myset1:
    print(x)

# union
union = myset1.union(myset2)

# superset
myset1.issuperset(myset2) # all elements of set2 are in set1

# subset
myset1.issubset(myset2) # all elements of set1 are inside set2 - it's reciprocal of superset 

# disjoint
myset1.isdisjoint(myset2) # no elements are similar in both sets


# copy of a list
myset1_copy = myset1 # Note: This is a soft copy i.e modification to this list will also modify the original
myset1_copy = myset1.copy() # Hard copy
myset1_copy = set(myset1)
myset1_copy = myset1[:]

# intersection
intersection = myset1.intersection(myset2)

# difference
diff = myset1.difference(myset2)
diff2 = myset1.symmetric_difference(myset2)

# update
myset1.update(myset2)
myset1.intersection_update(myset2)
myset1.difference_update(myset2)
myset1.symmetric_difference_update(myset2)

# add
myset1.add(10)

# remove
myset1.remove(10)
myset1.discard(15) # no error if element is not found
myset1.pop() # removes the first item from the set

myset2.clear()

# checking for an element in list
if 3 in myset1:
    print('yes')

# union





    
