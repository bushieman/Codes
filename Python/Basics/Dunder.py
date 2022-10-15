from queue import Queue as q

class Person:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f'name={self.name}'

    def __str__(self):
        return f'name={self.name}'

    def __mul__(self, x):
        self.name = self.name * x

    def __call__(self, y):
        print(y)

    def __len__(self):
        return len(self.name)

    def __add__(self, z):
       print(self.name + z)

    def __eq__(self, o):
        return self.name==o.name
       
person = Person('bush')
person2 = Person('bushman')
print(person==person2)
person + 'man'
print(len(person))
person * 10
person(21)
print(person)
print(len(person))

class Queue(q):
    def __repr__(self):
        return f'Queue={self._qsize()}'

    def __add__(self, item):
        self.put(item)

    def __sub__(self, item):
        self.get(item)
    
myqueue = Queue()
myqueue + 6
myqueue + 6
myqueue - 4
print(myqueue)
