class Human:
    def __init__(self, num, languages):
        self.var = num # this var is global inside the class Human
        self.lang = languages # this var is global inside the class Human

    def talk(self):

        print("humans speak",self.lang,"languages")


    def walk(self, legs):
        print("humans walk on", legs, "legs")


    def eat(self, food):
        print("humans like", food)


human = Human(2, 'many')
human.var
human.talk()
human.walk(human.var)
human.eat('pizza')



class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model 
        self.year = year

    def display(self):
        print(f"this is a {self.year} {self.make} {self.model}")


car = Car('ASTON MARTIN', 'db12', 2023)
car.display()



# static and class methods
class Person:
    marks = 300 # global attributes

    def __init__(self, name, age): #* constructor - Used to initialize/assign values to members of the class when an object of the class is created. The constructor may be of default type or parametized.
        self.name = name
        self.age = age 

    # SIMILARITY: class and static methods can be accessed directly without having to create instances of the class  i.e they are bound to the class and not the object of the class.
    # SIMILARITY: can take arguments
    # DIFFERENCE: class method has access to and can modify the attributes and methods defined in that class(global of that class) while a static method cannot
    # DIFFERENCE: class methods must take the cls attribute while static methods have the option to take the self attribute.
    # WHEN TO USE WHAT? 
        # we generally use class method to create factory methods. Factory methods return class objects ( similar to a constructor ) for different use cases.
        # We generally use static methods to create utility functions.
        
    def display(self):
        print(self.name, "is", self.age, "years old")
    
    @classmethod 
    def totalPoints(cls, correction):
        return cls.marks + correction


    @staticmethod # global method i.e defined inside the class Person
    def isAdult(age): 
        return age >= 18

    @classmethod 
    def adultAge(cls):
        return cls.isAdult(23)



person = Person('bushman', 21)
print(person.totalPoints(30)) 
print(person.isAdult(21)) 
print(Person.adultAge())
person.display() # note if i use print statement i will get my value and none since there is no return statement in my function.



def make_class(x):
    class Person:
        def __init__(self, name):
            self.name = name
        
        def details(self):
            print(self.name, 'is', x, 'years old')
        
    return Person

cls = make_class(21) # same as the actual class since a class object was returned
d = cls('bush') # create an instance of the class
print(d.name)
d.details()

## Inherit, extend, override
# Inheritance - process by which one class (child/derived) takes on the attributes and methods of another (parent/super) and can extend or overwrite them.
#@ Types of Inheritance:
    # Single inheritance: When a class inherits only one superclass
    # Multiple inheritance: When a class inherits multiple superclasses
    # Multilevel inheritance: When a class inherits a superclass, and then another class inherits this derived class forming a ‘parent, child, and grandchild’ class structure
    # Hierarchical inheritance: When one superclass is inherited by multiple derived classes
    
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):
        print(f'{self.name} is working')

class SoftwareEngineer(Employee): # inheritance
    def __init__(self, name, age, salary, level): # overwriting the init function from the parent class
        super().__init__(name, age, salary)
        self.level = level # extending

    def debug(self): # extending
        print(f'{self.name} is debugging')

    def work(self): # overwriting
        print(f'{self.name} is coding')

class Designer(Employee): # inheritance
    def draw(self): # extending
        print(f'{self.name} is drawing')

    def work(self):
        return self.work()

person1 = SoftwareEngineer('bushman', 21, 10000, 'Senior')
print(person1.name, person1.age)
print(person1.level)
person1.debug()
person1.work()
person2 = Designer('Rachel', 20, 7000)
person2.work()
person2.draw()

## Polymorphism - code that works on the superclass and will also work on the subclass as well
Employees = [SoftwareEngineer('bushman', 31, 10000, 'Senior'),
             SoftwareEngineer('Bravo', 21, 5000, 'Junior'),
             Designer('johnny', 19, 9000)
            ]

def motivate_employees(employees):
    for employee in employees:
        employee.work()
    
motivate_employees(Employees)

## Encapsulation - hiding of data implementation
class Programmer:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__salary = 5000 # private attribute (not accessible)
        self._pin = None # protected attribute (accessible)
        self._bugs_solved = 0
    
    # getter
    def get_salary(self):
        return self.__salary

    #  setter
    def set_salary(self, base_value):
        self.__salary = self._calculate_salary(base_value)

    @property # getter property - more efficient than the getter function
    def pin(self):
        return self._pin

    @pin.setter # setter property
    def pin(self, value):
        if isinstance(value, int):
            self._pin = value
        return self._pin

    # @pin.deleter
    # def pin(self):
    #     del self._pin

    def code(self):
        self._bugs_solved += 1

    def _calculate_salary(self, base_value):
        if self._bugs_solved < 10:
            return base_value
        elif self._bugs_solved < 100:
            return base_value * 2
        return base_value * 3

person = Programmer('bushman', 21)
for _ in range(70):
    person.code()

## Abstraction: Hides the internal implementatin of the code (_calculate_salary function)
person.set_salary(6000) 
print(person.get_salary())

person.pin = 1234
print(person.pin)

# We can use classes as objects to other classes by providing the object attribute
# I find it hard to use such objects with constructor functions

class Person(object):
    
    def name():
        return 'bushman'


class Employee():
    
    def __init__(self, Person):
        self.person =  Person
        
    def employee_name(self):
        return f'{self.person.name()} is a Tencent employee'
    
print(Employee(Person).employee_name())

# instantiating empty values
class Person():
    def __init__(self):
        self.details() # you can instantiate with empty objects or values
        self.name
        
        
    def details(self): # but make sure to assign their values
        self.name = 'bushman' # assigning values
        
        
    def names(self):
        return self.name
    
person = Person()
print(person.name)

