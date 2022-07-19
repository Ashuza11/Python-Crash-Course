"""
    M. Ashuza 
    july 19 2022
    Python Crash Course Book chapter 5 Exercises 
"""
# Qestion1 5-1. Conditional Tests


car = input("Give the car's name: ")
if car == "subaru":
    print("I predict True")
    print(f"The car is {car}.")
elif car == "audi":
    print("I predict False")
    print(f"The car is {car}.")
else:
    print(f"{car.title()} is not one of our marck.")
print("\n")

# Question 5-2. More Conditional Tests
my_name = "Ash"
my_wife_name = "Michelle"
if my_name == my_wife_name:
    print("This is really my sugnificant other")
elif my_name != my_wife_name:
    print(f"{my_wife_name.lower()} is not my wife.")
else:
    print("I do not know this name.")
print("\n")


age1 = 15
age2 = 20

if age1 > 10 and age2 > 18:
    print("You're a teen.")
elif age1 < 10 or age2 > 18:
        print("You're not a teen")

    
fruits = ["banan", "mango", "pinaple", "apple", "papaya"]
favrite_fruit = "orange"

if  favrite_fruit in fruits:
    print(f"{favrite_fruit.title()} is my favorite fruit.")
elif favrite_fruit not in fruits:
    print(f"{favrite_fruit.title()} is not my favorite fruit.")