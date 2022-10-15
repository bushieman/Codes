# Dictionary: key-value pairs, unordered, mutable
# creating a dictionary
mydict = {"name": "ken", "age": 21, "height":5.11}
mydict2 = dict(name = "bushman", age = 21, height = 5.11)

# assigning 
mydict['name'] = "bushman" # overwrites existing key
mydict['gender'] = "male" # creates new key if key does not exist

# deleting an item
del mydict['name']
mydict.pop('age')
mydict.popitem()

# accessing
print(mydict['height'])
print(mydict.get('key', 'return alternate if key not found'))
print(mydict)

# checking key in dictionary
try:
    print(mydict['name'])
except:
    print("key not found")

# looping 
for key in mydict2:
    print(key)
for value in mydict2.values():
    print(value)
for key,value in mydict2.items():
    print(key,value)

# copy
mydict3 = dict(mydict2)
mydict4 = mydict.copy()

# updating
mydict5 = dict(name = 'bushbaby', age = 22)
mydict2.update(mydict5)
print(mydict2)
print(mydict3)

# tuples as keys
mytuple = 8,7
mydict6 = {mytuple: 15} 
print(mydict6[8,7])

prices = {'bread': 55, 'sugar': 130, 'milk': 50}

min(prices, key=prices.get) # returns the key with the min value item
max(prices, key=prices.get) # returns the key with the max value item

# the optional keyword argument key that lets you specify a function that will be called on every element prior to sorting.
animals = [
    {'type': 'penguin', 'name': 'Stephanie', 'age': 8},
    {'type': 'elephant', 'name': 'Devon', 'age': 3},
    {'type': 'puma', 'name': 'Moe', 'age': 5}
]
sorted(animals, key=lambda animal: animal['age'])

# setdefault checks if key exists in our dict, and if so it returns that value. Otherwise, it sets dict['key'] to our 'value' and returns the new value
mydict.setdefault('key', 'value')

# merge two dicts
x = {'a': 1, 'b': 2}
y = {'b': 1, 'c': 5}
z = {**x, **y}
print(z) #@ note: the key 'b' get replaced instead of being updated
