# Need to import os first
import os

# rename (current, new)
#os.rename("write_tut3.txt", "write_tut2.txt")

# rename local directory python.py file
# Rename a file from python.py to python_rename.py
# (current, new)
#os.rename("new_file.py", "new_file2.py")

# Delete file Python_rename.py
#os.remove("new_file2.py")

# Directories Related Methods
# mkdir()
# Create directories in current directory

# Create a directory "python_test"
#os.mkdir("python_test")

# chdir() change current working directory
# Changing a directory to "C:/"
#os.chdir("C:/")
# In C:/ create a directory "test"
#os.mkdir("test")

# getcwd() will get current working directory
os.getcwd()


# Changing a directory to "C:/"
os.chdir("C:/")
# This would  remove "test"  directory.
os.rmdir("test")