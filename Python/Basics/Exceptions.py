age = int(input('Enter your age: '))

# error handling

if age < 1:
    raise Exception('Age should be greater than 0')

# assert terminates the code and raises an AssertionError which can take an assertion error message.
assert(age>=1), 'Age should be greater than 0'

try:
    age = int(input('Enter your age: '))
# # option 1
# except:
#     ValueError
# # option 2
# except:
#     print('Age must be an integer')
# # option3
# except Exception as e:
#     print(e)   
# # option 4
except ValueError:
    print('Age must be an integer'
# else runs only when there was no exception errors
else:
    print('perfect')
# finally runs no matter the code outcome
finally:
    print('test complete')

# creating unique errors
class ValueTooHighError(Exception):
    pass

def test_number(x):
    if x > 200:
        raise ValueTooHighError('age is too high')

age = int(input('Enter your age: '))

try:
    test_number(age)
except ValueTooHighError as v:
    print(v)
