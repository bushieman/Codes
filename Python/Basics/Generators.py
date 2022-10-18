# Generators return an object that can be iterated over
# are functions that return tuples
# Generator expressions are perfect for when you know you want to retrieve data from a sequence, but you don’t need to access all of it at the same time.
# The design allows generators to be used on massive sequences of data, because only one element exists in memory at a time.

import sys
def mygenerator():
    yield 1
    yield 2

g = mygenerator()
for i in g:
    print(i)

g = mygenerator()
value = next(g)
value = next(g)
print(value)


def countdown(num):
    print('starting')
    while num > 0:
        yield num
        num -= 1

for i in list(countdown(10)):
    print(i)
print('happy new year')

def number(num):
    return list(range(1, num+1))

print(sys.getsizeof(number(10)))

def gen_number(num):
    yield from range(1, num+1)

print(sys.getsizeof(gen_number(10)))

def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

for i in fibonacci(10):
    print(i)


# simplified generator expression
mygenerator = (i for i in range(100) if i%2 == 0)
print(sys.getsizeof(mygenerator))
mylist = [i for i in range(100) if i%2 == 0]
print(sys.getsizeof(mylist))

class Gen:
    def __init__(self, n):
        self.n = n
        self.last = 0

    def __next__(self):
        return self.next()

    def next(self):
        if self.last == self.n:
            raise StopIteration()
        rv = self.last ** 2
        self.last += 1
        return rv

g = Gen(100)

while True:
    try:
        print(next(g))
    except StopIteration:
        break

def gen(n):
    for i in range(n):
        yield i ** 2

g = gen(10)
value = next(g)
value = next(g)
value = next(g)
value = next(g)
value = next(g)
print(value)

for item in g:
    print(item)
