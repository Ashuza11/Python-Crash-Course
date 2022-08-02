"""
    M. Ashuza 
    july 26 2022
    Python Crash Course Book chapter 8 Exercises 
"""
from printing_fuction import display_message
# Question 8-1. Message
display_message()
print("\n")
# Question 8-2. Favorite Book

def favorite_book(title):
    print(f"One of my favorite books is {title.title()}")

favorite_book('python crash course')