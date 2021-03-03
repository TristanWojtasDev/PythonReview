# Functions
# Basic Rules:
# Begin with keyword def followed by function name and parenthesis
# Ex def DoSomething():
# Input parameters or arguments should be placed in parantheses

# Basic example

def example():
    print("This example will run")
    a = 22 + 99
    return a

print(example())

print("\n")

# Function required arguments
def printme(str):
   print (str) # This prints a passed string into this function
   return

# Now you can call printme function
printme("Hi there")


# Function Keyword arguments

def printme2(str, value):
   print (str) # This prints a passed string into this function
   print (value) # This prints a passed value into this function
   return

# Now you can call printme function
printme2(999, "Hi there2")
printme2("Hi there2",999)
print("\n")

# Default
def printme3(str, value = 77):
   print ("string:", str) # This prints a passed string into this function
   print ("value:", value) # This prints a passed value into this function
   return

# Now you can call printme function
printme3(value = 999, str = "Hi there")
printme3(str = "Hi there")
print("\n")

# Variable Length Arguments Functions
def printme4( args1, *args2 ):
   print ("Output is: ")
   print (args1)
   for var in args2:
      print (var)
   return

# Now you can call printinfo function
printme4( 10 )
printme4( 80, 70, 60, 50 )


# Anonymous lambda functions
# Dont use def, use lambda
# Lambda can take any number of arguments but return just one value
# Cannot print
# Own local namespace
# Ex
# lambda [arg1 [,arg2,.....argN]]:expression

sum = lambda arg1, arg2: arg1 + arg2
mult = lambda arg1, arg2: arg1 * arg2

# Now you can call sum and mult as a function
print ("Sum value:", sum(5, 10))
print ("Sum value:", sum(25, 25))
print ("Mult value:", mult(11, 11))
