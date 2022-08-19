
"""
    M. Ashuza 
    Auguest 15 2022
    Python Crash Course Book chapter 10 Exercises 
"""
# Question 10-6. Addition
print("Give me two numbers and i'll sum them.")

number_one = input("Give me the first number: ")

number_two = input("Give me the seconnd number: ")
try:
    result = int(number_one) + int(number_two)
except ValueError:
    print("You can't sum none interger ")
else:
    print(result)
print("\n")

# 10-7. Addition Calculator
print("Addintion calculator")
print("Print q to quit the program")

while True:
    number_one = input("Give me the first number: ")
    if number_one == 'q':
        break

    number_two = input("Give me the seconnd number: ")
    if number_two == 'q':
        break
    try:
        result = int(number_one) + int(number_two)
    except ValueError:
        print("You can't sum none interger ")
    else:
        print(result)
    


