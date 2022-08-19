"""
    M. Ashuza 
    Auguest 15 2022
    Python Crash Course Book chapter 10 Exercises 
"""
import json

# Question 10-12. Favorite Number Remembered
def get_stored_number():
    """Get favorite number if exixt"""
    file_name = 'favorite_numbers.json'
    try:
        with open(file_name) as f_object:
            number = json.load(f_object)
    except FileNotFoundError:
        return None 
    else:
        return number

def display():
    """Reads in the file content if exist and print message"""
    favorite_number = get_stored_number()
    if favorite_number:
        print(f"I know your favorite number! It’s {favorite_number}.")
    else:
        favorite_number = int(input("What's your favorite number?: "))
        file_name = 'favorite_numbers.json'
        with open(file_name, 'w') as f_object:
            number = json.dump(favorite_number, f_object)
            print(f"Your favorite number is {favorite_number} and it is stored now!")

display()
