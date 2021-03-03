# While Loop

print("Count is zero, iterate indented lines")
count = 0
while (count < 10):
   print ('Counter is:', count)
   count = count + 1

print ("We left while loop!")

# For Loop
# Ex 1 by character

for letter in 'Python':
   print ('Current Letter :', letter)

# Ex 2 by list
FruitList = ["Apple", "Avocado", "Banana", "Blackberry", "Blueberry", "Lemon", "Mango"]

for x in FruitList:
    print(x)

# Ex 3 by dictionary
Dict = {'Tomm':[25,'Alabama'], 'Bob':[28, 'California'], 'Alice':[21,'Florida'], 'Kevin':[35,'Delaware']}

for person in Dict:
    print(person, ' -> ', Dict[person])

# Ex 4 by number
for x in range(20,41):
    print(x)