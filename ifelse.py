# If Else

a = 10
b = 20

if a > b:
   print("a is more than b")
else:
   print("a is less than b")

print("\n")

# If Elif Else

a = 30
b = 20
c = 40

if a > b:
   print("a is more than b")
elif a < c:
   print("a is less than c")
else:
   print("there was something wrong")

print("\n")

# Nested If Elif Else
a = 10
b = 20
c = 0

if a > b:
   print("a is more than b")
elif b > c:
   if a == b:
      print("a is equal to b")
   else:
      print("a isn't equal to b")
else:
   print("there was something wrong")

print("\n")

# Breaking out of loops
for letter in "Python":
   if letter == 'o':
      break
   print ('Current Letter :', letter)

# Output should be Pyth

print("\n")

# Continue will skip that iteration but stay in loop
for letter in "Python":
    if letter == 'o':
        continue
    print("Current letter : ", letter)

# Should print Pythn

print("\n")

# Pass statement is used when
for letter in 'Python': 
   if letter == "o":
      pass
      print ("This is pass statement line")
   print ("Current Letter :", letter)