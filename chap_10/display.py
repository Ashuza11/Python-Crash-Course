"""
    M. Ashuza 
    Auguest 15 2022
    Python Crash Course Book chapter 10 Exercises 
"""
# Question 10-11. Favorite Number Print result
import json
from numbers import favorite_number

file_name = 'numbers.json'
def display(file_name):
    """Reads in the file content and print message"""
    favorite_number()
    with open(file_name) as f_object:
        number = json.load(f_object)
        print(f"I know your favorite number! It’s {number}.")

display(file_name)