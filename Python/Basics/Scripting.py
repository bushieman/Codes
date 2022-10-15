# system
import sys

sys.version # python version
sys.executable # shows the location of your python interpreter
sys.builtin_module_names # shows built-in modules available in python
sys.platform # platform
# print(sys.exit()) # safe exit
sys.argv # arguments passed to the script in the command line
sys.stdin # for interactive input like we use input(), raw_input(). Input is taken through stdin
sys.stdout # for output like print(), output is printed actually through stdout
sys.stderr # to prompt the error message
sys.setrecursionlimit(10) # limit the maximum depth of python interpreter. It helps you keep a stopover infinite recursion that can be a cause of overflow
sys.getdefaultencoding() # returns the default string encoding

# operating system
import os
os.name # name of the imported operating system dependent module
os.chdir("C:\\Users\\HP\\Downloads") # change the current working directory. Remember the double back-slash on your directory
os.getcwd() # get the current working directory
os.listdir("C:\\Users\\HP\\Downloads\\Scripts") # returns a list of all the files and folders in the specified directory. If no dir provided, it returns those of the CWD
# os.mkdir("C:\\Users\\HP\\Downloads\\Scripting") # creates a leaf directory in specific path provided it doesnot exist
# os.makedirs("C:\\Users\\HP\\Downloads\\Scripts\\main") # creates all missing intermediate directories linking to the leaf directory. use exist_ok=True parameter to ignore the error if the path already exists.
# os.remove("T:\\Codes\\Python\\Basics\\test.py") # removes a file path but not its directory which raises an error for the latter
# os.rmdir("C:\\Users\\HP\\Downloads\\Scripts\\main") # remove empty directory. If path not found, it raises an error
os.path.join("C:\\Users\\HP\\Downloads\\Scripts\\main", "") #  joins various path components into exactly one directory
os.path.split("C:\\Users\\HP\\Downloads\\Scripts\\main") # returns a tuple of head-the first section of the path and tail-the last pathname component
os.path.exists("C:\\Users\\HP\\Downloads\\Scripts\\main") # finds if the path exists or not
os.path.dirname("C:\\Users\\HP\\Downloads\\Scripts\\main") # returns the directory name from the path given
os.path.basename("C:\\Users\\HP\\Downloads\\Scripts\\main") # get the base name in a specified path
print(os.environ) # it is a mapping object that represents the string environment when the os module is initially imported
os.stat_result(True) # returns the statistics

## other scripting modules include
#> math module
import math

math.perm(n) # choose n values without repeating and with order i.e (123 not same as 321); thus math.perm(3) = 6 i.e 123, 132, 213, 231, 312, 321
math.perm(n, k) # choose k possible values from n without repeating and with order; thus math.perm(3, 2) = 6 i.e 12, 13, 21, 23, 31, 32

math.comb(n, k) # choose k possible values from n without repeating but without order; thus math.comb(3, 2) = 6 i.e 12, 13, 23

math.floor(x)
math.ceil(x)

math.factorial(x) # returns x * x-1 * x-2 * ..... * 1
math.pi # utility for pi
math.pow(x, y)  # returns x ** y 
math.prod([x, y, z]) # returns x * y * z 

#> random module
#> subprocess module
#> datetime module
#> json module
