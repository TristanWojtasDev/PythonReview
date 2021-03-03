# Classes
# Example Syntax


#class ClassName:
#   'Optional class documentation string'
#   class_suite

# Classes have a documentation string that can be accessed through ClassName.__doc__.
# Class_suite usually consistens of all the component statements defining:
# Class members
# Data Attributes
# Functions
# Self represents instance of class

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

class Person2:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person2("John", 36)
p1.myfunc()