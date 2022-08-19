"""
    M. Ashuza 
    Auguest 14 2022
    Python Crash Course Book chapter 10 Exercises 
"""
# Question 10-1. Learning Python

filename = 'learning_python.txt'

# Reading in the entire file
with open('learning_python.txt') as file_object:
    contents = file_object.read()
    print(contents)
print("\n")

# Looping over the fileobject 
with open(filename) as f_object:
    for line in f_object:
        print(line.rstrip())

print("\n")

# Storing the lines in a list and then working with them outsidethe with block
with open(filename) as f_obj:
    lines = f_obj.readlines()

for line in lines:
    print(line.strip())
print("\n")
# Question 10-2. Learning C++
with open(filename) as f_obj:
    lines = f_obj.readlines()

for line in lines:
    changed = line.replace('python', 'c++')
    print(changed.rstrip())

