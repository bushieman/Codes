import copy
org = 10 # immutable item int
cpy = org
cpy = 1 # creates a new variable independent of the other copy var
print(cpy)
print(org)

orglist = [1, 2, 3, 4, 5] # mutable item
cpy = orglist
cpy[0] = -1
print(cpy)
print(orglist)

# shallow copy: one level deep, only references of nested child objects
orglist = [1, 2, 3, 4, 5]
cpy = orglist.copy()
cpy2 = copy.copy(orglist)
cpy3 = list(orglist)
cpy4 = orglist[:]
cpy4[0] = -1
print(cpy4)
print(orglist)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person('bush', 21)
person2 = copy.copy(person1)
person2.age = 24
print(person1.name, person1.age)
print(person2.name, person2.age)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person('elon', 54)
person2 = Person('bush', 21)


class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee

company = Company(person1, person2)
companyclone = copy.copy(company)
companyclone.boss = {'name': 'musk','age': 56}
print(company.boss.name, company.boss.age)
print(companyclone.boss['name'], companyclone.boss['age'])

# deep copy: full independent copy
orglist =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
cpy = copy.deepcopy(orglist)
cpy[0] [1] = 20
print(cpy)
print(orglist)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person('elon', 54)
person2 = Person('bush', 21)


class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee

company = Company(person1, person2)
companyclone = copy.deepcopy(company)
companyclone.boss.age = 56
print(company.boss.name, company.boss.age)
print(companyclone.boss.name, companyclone.boss.age)

