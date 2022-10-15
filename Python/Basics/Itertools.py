# product
import operator
from itertools import combinations_with_replacement, groupby, product, permutations, combinations, accumulate, count, cycle, repeat
a = [1, 2, 3]
b = [6, 7, 5]
c = [1, 2, 9]

prod = product(a,b,c)
print(list(prod))

# permutations
#@ With permutations, the order of the elements matters and so (1,2) is not the same as (2,1) and hence will return two values
a = [1, 2, 3]
perm = permutations(a, 2)
print(list(perm))

# combinations
#@ with combinations, the order of the elements doesn't matter and so (1,2) is same as (2,1) and will return only one value
a = [1, 2, 3, 4]
comb = combinations(a, 3)
print(list(comb))
comb_wr = combinations_with_replacement(a,3)
print(list(comb_wr))

# accumulate
a = [1, 2, 3, 4]
acc = accumulate(a)
print(list(acc))
acc_mul = accumulate(a, func=operator.mul)
print(list(acc_mul))
a = [1, 5, 2, 3, 4]
acc_max = accumulate(a, func=max)
print(list(acc_max))

# groupby
a = [1, 2, 3, 4]
groupby_obj = groupby(a, key=lambda x: x < 3)
for key, value in groupby_obj:
    print(key, list(value))

# # count
# for i in count(1, 2): # provides  a start, step infinite loop

# # cycle
# a = [1, 2, 3, 4, 5]
# for i in cycle(a): # provides an infinite loop of an iterable object

# repeat
for i in repeat(1, 5):
    print(i) 

# itertools.product() can replace nested for loops
for key, name in enumerate(members):
    for age in age_list:
        if age[key] > 18:
            print(f'{name} is an adult')
        else:
            print(f'{name} is a kid')
            
for (key, name), age in product(enumerate(members), age_list):
    print(f'{name} is an adult') if age[key] > 18 else print(f'{name} is a kid')
