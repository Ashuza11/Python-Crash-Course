"""
    M. Ashuza 
    july 23 2022
    Python Crash Course Book chapter 7 Exercises 
"""

# Question 7-4. Pizza Toppings

topping = ""
print("Inter quit to end the programm\n")
while topping != 'quit':
    topping = input("Inter the Pizza name: ")
   
    if topping != 'quit':
         print(f"You’ll add {topping.title()} to your pizza")
print("Thak you")
print("\n")

# Question 7-5. Movie Tickets

play = True
mesage = ""
print("Inter Yes to continue or Non to quit the programm.\n")
while play:
    age = int(input("Inter Your age please!: "))
   
    if mesage != 'yes':
        if age < 3:
            print("Your ticket is free")
        elif age >= 3 and age < 12:
            print("Yout ticket is 10$")
        elif age > 12:
            print("Your ticket is 15$")
        mesage = input("Would you like to buy enother ticket? Yes/Non: ")
    if mesage == "nom":
        play = False
    print("Thak you for buying a ticket")
print("\n")

# Question 7-6. Three Exits

active = True
topping = ""
print("Inter quit to end the programm\n")
while active:
    topping = input("Inter the Pizza name: ")
   
    if topping == 'quit':
        break
    else:
        print(f"You’ll add {topping.title()} to your pizza")
print("Thak you")
print("\n")

# Question 7-7. Infinity

number = 1
while number < 5:
    print("Helllo")


# Question 7-8. Deli

sandwich_orders = [
    'Chicken Sandwich', 'Egg Sandwich', 
    'Seafood Sandwich', 'Roast Beef Sandwich',
    'Grilled Cheese','Ham Sandwich',
    'Nutella Sandwich','Grilled Chicken Sandwich'
    ]

finished_sandwiches = []
while sandwich_orders:
    current_sandwiches = sandwich_orders.pop()
    print(f"I made your {current_sandwiches}.")
    finished_sandwiches.append(current_sandwiches)
print("\n The following sandwich has been made you:")
for sandwich in finished_sandwiches:
    print(sandwich)
print("\n")

# 7-9. No Pastrami

sandwich_orders = [
    'Chicken', 'Egg', 
    'pastrami', 'Roast Beef',
    'pastrami','Ham',
    'Nutella', 'pastrami' 
    ]
print("The Deli has run out of pastrami sandwich")

while sandwich_orders:
    current_sandwichies = sandwich_orders.pop()
print(sandwich_orders)

# Question 7-10. Dream Vacation

print("This is a poll about your dream placies for vacation")
print("Enter Yes/Non to play.\n")

active = True
play = 'yes'
placies = []

while active:
    if play == 'yes':
        place = input("Inter the name of the place: ")
        placies.append(place)
        poll_result = placies[:]
    print("Are you done ? Yes/Non.")
    play = input("Answer: ")
    if play == 'yes':
        print(poll_result)
        continue
    else:
        break
print("The final result for the poll is: ")
for result in poll_result:
    print(result.title())

