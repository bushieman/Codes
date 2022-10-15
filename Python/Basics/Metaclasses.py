class Foo:
    def show(self):
        print('hello')

def func(self):
    self.z = 15

Test = type('Test', (Foo,), {'x': 5, 'func': func}) # name, basis, attributes
t = Test()
t.y = 10
print(t.x)
print(t.y)
t.show()
t.func()
print(t.z)

# metaclass
class Meta(type):
    def __new__(self, classname, bases, attr):
        ATTR = {}
        for key, value in attr.items():
            if key.startswith('__'):
                ATTR[key] = value
            else:
                ATTR[key.upper()] = value
        return type(classname, bases, ATTR)

class Dog(metaclass=Meta):
    walk = 'walk'
    bark = 'bark'

    @classmethod
    def barking(cls):
        return cls.BARK

    def hello(self):
        print('hello')

dog = Dog()
print(dog.BARKING())
dog.HELLO()
