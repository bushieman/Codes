# decorators extend the behaviour of a function
import functools
import time

# function decorators structure
def dosomething(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('start')
        func(*args, **kwargs)
        print('end')
    return wrapper

@dosomething
def square(x):
    print(x ** 2)

square(10)

# timer decorator
def timer(func):
    def wrapper():
        start = time.time()
        func()
        total = time.time() - start
        print('time: ', total)
    return wrapper

@timer
def test():
    for _ in range(100000):
        pass

@timer
def test2():
    time.sleep(2)

test()
test2()


# decorators with arguments
def repeat(times=3):
    def dosomething(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                results = func(*args, **kwargs)
                print(f'hello', results)
            return results
        return wrapper
    return dosomething

@repeat(times=3)
def greet(name):
    return name
greet('ken')


# nested decorators
def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('started debugging')
        func(*args, **kwargs)
        print('finished debugging')
    return wrapper


def naming(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        name = func(*args, **kwargs)
        print('hi', name)
    return wrapper

@debug 
@naming
def myname(name):
    return name

myname('ken')


# class decorators
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kargs):
        self.num_calls += 1
        name = self.func(*args, **kargs)
        print(name,'was executed', self.num_calls, 'times')
    
    def last(self):
        print('last name')

@CountCalls
def myname(name):
    return name

for _ in range(10):
    myname('ken')

myname.last()


