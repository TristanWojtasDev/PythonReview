# Can do most manipulation with file object
# Before you can read or write a file, you must open it using
# Pythons built in open()
# File method provides a set of access methods

# Syntax
# file object = open(file_name [, access_mode][, buffering])
# file_name is a string value that contains name of file to access
# access_mode is mode in which file has to be opened, read, write, append, etc
# access_mode is optional
# buffering, if set to - no buffering takes place
# if buffering is set to 1, line bufferring is performed while accessing file
# greater than 1 is that buffer, negative is default system buffer

# different modes for opening file
# r read only
# rb read only binary format
# r+ reading writing
# rb reading writing binary format
# wb writing binary, will overrite original if exists
# w+ reading writing, will overrite if exists
# wb+ writing reading binary format, overwrites if exists
# a opens file for appending
# ab opens a file for appending in binary
# ab opens a file for appending in binary
# a+ opens file for both appending and reading
# a+ opens file for both appending and reading in binary

# write() to file method
# you need to add newline yourself

# changing w to a will allow you to add to text file rather than just overrite it

# At first we must open file
file = open("write_tut.txt", "w")
# Write anything you want
file.write( "This is python write to file tutorial.\nWe will learn it!\n")
# Always close file
file.close()


# At first we must open file
file = open("write_tut.txt", "r")
# Read everything from file and print
print(file.read())
# Always close file
file.close()


# Open a file
file = open("write_tut.txt", "r+")
# Read a file
string = file.read()
print ("Read String is:", string)
# Check current position
position = file.tell()
print ("Current file position:", position)
# Reposition pointer where we need
position = file.seek(55,0)
# Read string from pointer
string2 = file.read()
# Reposition pointer again
position = file.seek(55,0)
# Write new line and add string2 
file.write("\nInserting new line to text."+string2)
# Check if everything worked
file.seek(0,0)
print ("\nFull string:", file.read())
# Close opened file
file.close()