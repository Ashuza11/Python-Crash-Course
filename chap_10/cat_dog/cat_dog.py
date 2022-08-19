"""
    M. Ashuza 
    Auguest 15 2022
    Python Crash Course Book chapter 10 Exercises 
"""
# Question 10-8. Cats and Dogs
file_names = ['dogs.txt', 'cats.txt']

def print_file_content(file_name):
    """Print files content"""
    try:
        with open(file_name) as file_objects:
            content = file_objects.read()
    except FileNotFoundError:
        print(f"File {file_name} does not exist.")
    else:
        print("List of animals")
        print(content)


for file_name in file_names:
    print_file_content(file_name) 

# Quuestion 10-9. Silent Cats and Dogs
def print_file_content(file_name):
    """Print files content"""
    try:
        with open(file_name) as file_objects:
            content = file_objects.read()
    except FileNotFoundError:
        pass
    else:
        print("List of animals")
        print(content)


for file_name in file_names:
    print_file_content(file_name) 
