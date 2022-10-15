import json
from json import JSONEncoder

person = {'name': 'Bushman', 'age': 21, 'city': 'Nairobi', 'hasChildren': False, 'titles':['engineer', 'programmer']}

personJSON = json.dumps(person, indent=4, sort_keys=True)

# object to json data
with open('profile.json', 'w') as file:
    json.dump(person, file, sort_keys=True, indent=4)

# json data to object
# from the same file
person = json.loads(personJSON) 
print(person)

# from a json file
with open('profile.json', 'r') as file:
    person = json.load(file)
    print(person)


# class instance
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User('bushbaby', 21)

# create an encoding function
def encode_user(o):
    if isinstance(o, User):
        return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
    else:
        raise TypeError('Object of type User is not JSON serializable')
    
# using a json encoder
class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)


userJSON = json.dumps(user, default=encode_user)
userJSON2 = json.dumps(user, cls=UserEncoder)
userJSON3 = UserEncoder().encode(user)
print(userJSON)
print(userJSON2)
print(userJSON3)


# decoder
def decode_user(dic):
    if User.__name__ in dic:
        return User(name=dic['name'], age=['age'])
    return dic


user = json.loads(userJSON, object_hook=decode_user)
print(user.name)
