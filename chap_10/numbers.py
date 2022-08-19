"""
    M. Ashuza 
    Auguest 15 2022
    Python Crash Course Book chapter 10 Exercises 
"""
"""Take in unser input and stores it in a json file"""
import json

# Question 10-11. Favorite Number
file_name = 'numbers.json'

def favorite_number():
    """Prompts for a number ans stores it in a file"""
    number = int(input("What's your favorite number?: "))
    with open(file_name, 'w') as f_object:
        json.dump(number, f_object)





