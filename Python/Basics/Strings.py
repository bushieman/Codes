# Strings: ordered, immutable, text representation

# creation
string1 = 'bushman'
string2 = "bushman"
string3 = '''my 
name 
is 
bushman''' # triple quotes are used for multi-line strings

# the str method stringifyies every char inside a string or integer
num = str(10)
name = 'bushman'
print(num)
print(name)

# list to string
mylist = ['bushman', 'bush', 'bushieman', 'bushbaby']
string4 = ' also '.join(mylist)
print(string4)

# accessing strings
string1[0]

# slice operator
string1[::]

# reversing strings
string1[::-1]

# iterate over the string
for x in string1:
    print(x)

# checking for a char or substring in string
if 'ush' in string1:
    print('yes')

# string methods
string1.strip() # removes the white spaces inside a string
len(string1)
string1.upper()
string1.lower()
string1.split(',') # splits the string on the delimiter.space is the default setting
string1.split(',', n=1, expand=True) # n is the number of splits, expand creates a new df of the splitted items
string1.startswith('b')
string1.endswith('b') # both startswith and endswith are case sensitive and can take a char or a substring
string1.find('ma')
string1.count('b')
string1.replace('b', 'k')
string1.replace('[', '', regex=True)

# modifying strings
name = 'ken'
age = 21
height = 5.113455654665
# %
sentence = 'My name is %s. I am %d. I am %.2f feet tall' %(name, age, height)
print(sentence)
# .format()
sentence = 'My name is {}. I am {}. I am {:.2f} feet tall' .format(name, age, height)
print(sentence)
# f format
# The one risk to be aware of this format is that if you’re outputting user­ generated values, then that can introduce security risks, in which case Template Strings may be a safer option.
sentence = f'My name is {name}. I am {age}. I am {height} feet tall'
print(sentence)

print('He gets a monthly salary of {:,}'.format(8000*30)) # thousands separator
print('He gets a monthly salary of {:_}.'.format(8000*30)) # thousands separator
print('The room measures {:,.2f} and {:,.3f} inches.'.format(30.573839, 45.43576)) # round off to 2dp and 3dp respectively

import string # string module

# methods
string.punctuation
string.digits
string.ascii_uppercase
string.ascii_lowercase
string.capwords('bushman anampius')

#* String constants
import string

print(string.ascii_letters)
print(string.ascii_uppercase)
print(string.ascii_lowercase)
print(string.digits)
print(string.hexdigits)
print(string.octdigits)
print(string.punctuation)
print(string.printable)
print(string.whitespace)

# strip
mystring = ' This is my string '
print(f'start here:{mystring.rstrip()}.') # strips  the whitespace on the right side
print(f'start here:{mystring.lstrip()}.') # strips the whitespace on the left side
print(f'start here:{mystring.strip()}.') # strips the whitespace on both sides
