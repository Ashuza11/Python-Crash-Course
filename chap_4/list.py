"""
    M. Ashuza 
    july 5 2022
    Python Crash Course Book chapter 4 Exercises 
"""
# Qestion1 4-1. Pizzas
import numbers


my_favorite_pizzas = ['Neapolitan  Pizza', 'Chicago Pizza', 'New York-Style Pizza', ' Sicilian Pizza', 'Greek Pizza']
   
for pizza in my_favorite_pizzas:
    print(f"I like  {pizza}.")
print("\nI really love pizza!\n")

# Question2 4-2. Animals
animals = ['cat', 'dog', 'rabbit', 'cow']

for index, animal in enumerate(animals):
    print(f"Here is the animal number {index}, and it's called {animal}.")
   
print("\n Any of these animals would make a great pet!")
    

# Question3 4-3. Counting to Twenty
for i in range(21):
    print(str(i) + "\n")

# Question 4-4. One Million
numbers = []
for number in range(1, 1000001):
    numbers.append(number)

for num in numbers:
    if num == 101:
        print(f"We've reached {num} number terminationg loop")
        break
    print(num)


   

# Question5 4-5. Summing a Million
numbers = []
for number in range(1, 1000001):
    numbers.append(number)
    

print(f"\n The first number is {min(numbers)}")
print(f"The last number is {max(numbers)}")
print(f"The sum of all numbers are {sum(numbers)}\n")

## Same dolution with list comprihesion 
a_million_numbers = [number for nomber in range(1, 1000001) ]
print(f"The first number is {min(numbers)}")
print(f"The last number is {max(numbers)}")
print(f"The sum of all numbers are {sum(numbers)}\n")


# Question6 4-6. Odd Numbers
odd_numbers = [num for num in range(1, 20, 2)]
for number in odd_numbers:
    print(number)
print("\n")

# Question7 4-7. Threes
multiple_of_three = [num for num in range(3, 30, 3)]
for number in multiple_of_three:
    print(number)
print("\n")

# Question8 4-8. Cubes
cubes = []
for num in range(1, 10):
    cubes.append(num**3)
for num in cubes:
    print(num)
print("\n The same dolution with list comprehession")
## Same dolutin with list comprehension
cubes = [num**3 for num in range(1, 10)]
for num in cubes:
    print(num)