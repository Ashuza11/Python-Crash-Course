"""
    M. Ashuza 
    july 26 2022
    Python Crash Course Book chapter 8 Exercises 
"""

# Question 8-1. Message
def display_message():
    print("Hello everyone i am learning about functions.")
    
display_message()
print("\n")
# Question 8-2. Favorite Book

def favorite_book(title):
    print(f"One of my favorite books is {title.title()}")

favorite_book('python crash course')