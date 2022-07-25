"""
    M. Ashuza 
    july 23 2022
    Python Crash Course Book chapter 7 Exercises 
"""

# Question 7-1. Rental Car

car_name = input("What kind of car do you like?: ")
print(f"Let me see if I can find you a {car_name.title()}")

# Question 7-2. Restaurant Seating
people_number = int(input("How many people are in their dinner group? : "))

if people_number > 8:
    print("You have to wait for a table please!")
else:
    print("Welcom budies your table is ready.")
print("\n")

# Question 7-3. Multiples of Ten

number = int(input("Inter a number and I'll tell you whether it's a multiple of ten : "))

if number % 2 == 0:
    print(f"The number {number} is a multiple of 10")
else:
    print(f"The number {number} is not a multiple of 10")
print("\n")
