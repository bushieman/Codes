from collections import Counter
from collections import defaultdict

# * Counter
# creating
counter1 = Counter({'a':1, 'b':2})
counter2 = Counter('bushman')
counter3 = Counter(['a', 'b'])
counter4 = Counter(a=3, b=2)

words = "If there was there was but if there was not there was not".split(' ')
counter5 = Counter(words)
print(counter5)

# accessing
counter1['c']
counter1.keys()
counter1.values()
counter1.items()

# useful methods
counter1.most_common(1) #@ returns the n most frequent inputs by count.
counter1.elements()
counter1.clear()

# subtract
a= Counter(chicken=6,cats=3,dogs=4)
b = Counter({"chicken":2, "cats":1, 'dogs': 5})
c = Counter(["chicken", "cats", 'dogs'])
print(a+b+c)
print(a-b-c)
a.subtract(b)
print(a)

# add
a= Counter(chicken=6,cats=3,dogs=4)
b = Counter({"chicken":2, "cats":1, 'dogs': 5})
a.update(b)
print(a)

# intersection - the minimum elements between both of our lists
a= Counter(chicken=6,cats=3,dogs=4)
b = Counter({"chicken":2, "cats":1, 'dogs': 5})
print(a&b)

# union - the maximum elements in both of our lists
a= Counter(chicken=6,cats=3,dogs=4)
b = Counter({"chicken":2, "cats":1, 'dogs': 5})
print(a|b)

# * defaultdict
# defaultdict are similar to normal dict with the main difference being that when you try to access or modify a key that's not present in the dictionary, a default value is automatically given to that key .
person = defaultdict(list) #@ notice the argument
person['name'] = 'bushman'
person['maths'].append(94)
person['maths'].append(90)
person['maths'].append(86)
person['maths'].append(92)

print(person['name'])
print(person['maths'])
print(person['science'])

# defaultdict with custom functions
import time

def evaluate():
    mylist = []
    print('Evaluating...........')
    time.sleep(3)
    return 'item not found'

person = defaultdict(evaluate)

print(person['name'])

# defaultdict with lambda functions
person = defaultdict(lambda : 'person detail not found')

print(person['name'])

# You can also use a lambda function as your factory value to return an arbitrary constant.
mydict = defaultdict(lambda x: type(x))

mydict['name'] = 'bushman'
mydict['grades'] = ['A-']
mydict['grades'].append('B+')

#* deques
# This library has the methods for adding and removing elements which can be invoked directly with arguments.
from collections import deque

# Create a deque
DoubleEnded = deque(["Mon","Tue","Wed"])
DoubleEnded.append("Thu") # Appending to the right
DoubleEnded.appendleft("Sun") # Appending to the left
DoubleEnded.pop() # Remove from the right
DoubleEnded.popleft() # Remove from the left
DoubleEnded.reverse() # Reverse the deque
