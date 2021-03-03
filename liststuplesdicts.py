# Lists
# Items separated by commas with square brackets
# Array but with different datatypes

list = ['qwerty', 7777, 1.11, 'Tomm', 66.6]
tinylist = [987, 'Tomm']
print("Prints complete list - print (list)")
print (list)
print("\n")
print("Prints first element of the list - print (list[0])")
print (list[0])
print("\n")
print("Prints elements starting 1st and 2nd index not 3rd - print (list[1:3])")
print (list[1:3])
print("\n")
print("Prints list starting from 2nd index on - print (list[2:])")        
print (list[2:])
print("\n")
print("Prints the list two times - print (tinylist * 2)")
print (tinylist * 2)
print("\n")
print("Prints concatenated list")
print (list + tinylist)

print("\n")
print("\n")
# Tuples
# Enclosed with parenthesis not brackets, length cannot be changed
# View as read only lists

print("Tuples")

tuple = ('qwerty', 7777, 1.11, 'Tomm', 66.6)
tinytuple = (987, 'Tomm')

print("Prints complete tuple - print (tuple)")
print (tuple)
print("\n")
print("Prints first element of the tuple - print (tuple[0])")
print (tuple[0])
print("\n")
print("Prints 1st and 2nd index - print (tuple[1:3])")
print (tuple[1:3])
print("\n")
print("Prints tuple starting from 3rd character - print (tuple[2:])")
print (tuple[2:])
print("\n")
print("Prints tuple two times - print (tinytuple * 2)")
print (tinytuple * 2)
print("\n")
print("Prints concatenated tuple - print (tuple + tinytuple)")
print (tuple + tinytuple)

print("If we try to update a tuple like tuple[2] = 200 we get type error 'tuple'")

print("\n")
# Dictionary
# Associative arrays. Non-ordered key value pairs
# Key can be any type but usually int or string
# Value can be anything including an object
# Defined by curly braces
# Values assigned and accessed using square braces


print("Dictionary")
print("\n")

dict = {}
dict['first'] = "This is first"
dict[2] = "This is second"

tinydict = {'name': 'Tomm', 'code':6434, 'hobby':'reading'}

# Prints value of dictonary dict based on key 'first'
print(dict['first'])

# Prints value of dictonary dict based on key 2
print(dict[2])

# Prints entire key value pair of dict tinydict
print(tinydict)

# Prints keys only of tinydict dict
print(tinydict.keys())

# Prints values only of tinydict dict
print(tinydict.values())

# Add new value to tinydict
tinydict['City'] = 'London'

# Print tinydict
print(tinydict)

# Delete key value pair by key code
del tinydict['code']

# Print tinydict
print(tinydict)

# Multidimensional Dict
Dict = {'Tomm':[25,'Alabama'], 'Bob':[28, 'California'], 'Alice':[21,'Florida'], 'Kevin':[35,'Delaware']}

# Print All Values of Key 'Kevin'
print(Dict['Kevin'])

# Print 1st indexed(2nd) value of Key 'Bob'
print(Dict['Bob'][1])