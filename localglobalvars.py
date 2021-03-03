# Local vs Global
# Mixed Ex              

total = 5 # This is global variable.
def sum(arg1, arg2):
   total = arg1 + arg2 # Here total is local variable.
   print ("Inside the function local total:", total)
   return total

# Now you can call sum function
sum(17, 19)
print ("Outside the function global total:",total)


# Global Ex
x = 10
def example():
    print(x)

example()

# How to edit global variables locally

x = 10
def exampleEditGlobal():
    # what we do here is defined x as a global variable. 
    global x
    x += 5
    print(x)

exampleEditGlobal()
print(x)

# A different way to edit global variables locally

x = 10
def exampleEditGlobalB(x):
    x += 5
    return x

x = exampleEditGlobalB(x)
print(x)