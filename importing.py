# Modules
# File consisting of Python Code
# When you import, you are basically loading that module into memory
# When python encounters an import statement,
# It imports it based in search path, which is a list of directories
# Searchs current directory, then each directory in shell variable PYTHONPATH
# If those both fail, Python checks default path

# Ex
# Import module statistics
import statistics

# Or we can create our own module, by adding it to local python project folder
# Add this code as printing.py with following code:
#def print_func(parameter):
#   print ("Printing:", parameter)
#   return

# We can import this module by
import printing

# Now you can call defined function that module as follows
printing.print_func("Welcome to import tutorial")

# or can use As
# Import module support
import printing as p

# Now you can call defined function that module as follows
p.print_func("Welcome to import tutorial")


# Examples of how to keep your imports clean
# Instead of this 

# Import module statistics
import statistics

example_list = [5,2,5,6,1,2,6,7,2,6,3,5,5]
print(statistics.variance(example_list))

# You can do this
from statistics import variance as var

example_list = [5,2,5,6,1,2,6,7,2,6,3,5,5]
print(var(example_list))

# This will allow you to skip the file name prefix
#from statistics import *

#example_list = [5,2,5,6,1,2,6,7,2,6,3,5,5]
#print(variance(example_list))

# Reload function
# If you editted the source file and want a new fresh instance use reload
#reload(statistics)

# The dir() function
# Returns a softed list of strings containing names defined by module

# Import built-in statistics module
import statistics

content = dir(statistics)
print (content)

# Here the special string variable __name__ is the modules name, __file__
# is where the filename of the module is