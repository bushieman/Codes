# We can use the argparse module to create a basic command line interface
from argparse import ArgumentParser, Namespace

# # Basic parser
# #* instantiate the parser
# parser = ArgumentParser()
# #* add arguments
# parser.add_argument('square', help='Squares a given number', type=int) # created the square variable
# #* retrieve the parser
# args = parser.parse_args()
# #* display output in console
# print(args.square**2)


# Positional Arguments
#@ Actions
# parser = ArgumentParser()
# parser.add_argument('square', help='Squares a given number', type=int)
# parser.add_argument('-v', '--verbose', action='store_true') # -v for short version of --verbose, action=store_true stores a boolean which we can manipulate later
# args = parser.parse_args()

# if args.verbose:
#     print(f'The square of {args.square} is {args.square**2}')
# else:
#     print(args.square**2)

#@ Choices
# parser = ArgumentParser()
# parser.add_argument('square', help='Squares a given number', type=int) 
# parser.add_argument('-v', '--verbose', type=int, choices=[0,1,2]) 
# args = parser.parse_args()

# if args.verbose==0:
#     print(args.square**2)
# elif args.verbose==1:
#     print(f'The square of {args.square} is {args.square**2}')
# elif args.verbose==2:
#     print(f'The square of {args.square} is {args.square**2}.\nThis is because the square of a number is the same as the number multipled by itself.\nTherefore {args.square}^2 -> {args.square}*{args.square} = {args.square**2}')

#@ Defaults
parser = ArgumentParser()
# use default parameter to handle missing arguments. 
# Default must take an extra argument nargs ie the no of arguments you expect
parser.add_argument('square', help='Squares a given number', type=int, default=2, nargs='?')
parser.add_argument('-v', '--verbose', help='Verbose description. Use -vv for extra verbose', action='count') # action=count tallies the no of v's in the argument
args = parser.parse_args()

if args.verbose==1:
    print(f'The square of {args.square} is {args.square**2}')
elif args.verbose==2:
    print(f'The square of {args.square} is {args.square**2}.\nThis is because the square of a number is the same as the number multipled by itself.\nTherefore {args.square}^2 -> {args.square}*{args.square} = {args.square**2}')
else:
    print(args.square**2)

