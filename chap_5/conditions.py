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

print("\n")
# Question 5-3. Alien Colors #1
alien_color = 'green'

if alien_color == 'green':
    print("You just earned 5 points.")

alien_color = 'red'
if alien_color != 'yellow':
    print("fails.")
print("\n")

# Question 5-4. Alien Colors #2I
    # With if - if chane 
alien_color = 'green'

if alien_color == 'green':
    print("You just earned 5 points for shooting the alien.")
if alien_color != 'green':
    print("You just earned 10 points.")
print("\n")  
 
# Question 5-5. Alien Colors #3
alien_color2 = "yellow"

if alien_color2 == "green":
    print("The player has earned 5 points.")
elif alien_color2 == "yellow":
     print("The player has earned 10 points.")
elif alien_color2 == "red":
     print("The player has earned 15 points.")

# Question 5-6. Stages of Life:
age = 1
# If the person is less than 2 years old, print a message that the person is baby
# • If the person is at least 2 years old but less than 4, print a message that
# the person is a toddler.
# • If the person is at least 4 years old but less than 13, print a message that
# the person is a kid.
# • If the person is at least 13 years old but less than 20, print a message that
# the person is a teenager.
# • If the person is at least 20 years old but less than 65, print a message that
# the person is an adult.
# • If the person is age 65 or older, print a message that the person is an
# elder.
if age < 2:
    print("You're a baby")
elif age == 2 or age < 4:
    print("You're a toddler")
elif age == 4 or age < 13:
    print("You're a kid")
elif age == 13 or age > 20:
    print("You're a teenager")
elif age == 20 or age <= 65:
    print("You're an adult") 
elif age >= 65:
    print="You're elder"
print("\n")

# Question 5-7. Favorite Fruit
favorite_fruits = ["orage", "banana", "avocado", "lemon", "pinapple", "apple"]

if "orage" in favorite_fruits:
    print(f"My first favorite fruit is {favorite_fruits[0].title()}.")
if favorite_fruits[1] in favorite_fruits:
    print(f"My first favorite fruit is {favorite_fruits[1].title()}s.")
if "avocado" in favorite_fruits:
    print("You really like" + favorite_fruits[2].title() + " !")
if "lemon" in favorite_fruits:
    print(f"You really like {favorite_fruits[3].title()}s !")
print("\n")


