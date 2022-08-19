
"""
    M. Ashuza 
    Auguest 14 2022
    Python Crash Course Book chapter 10 Exercises 
"""
# Question 10-5. Programming Poll
file_name = 'poll.txt'

number_of_people = 0
while number_of_people < 5:
    name = input("What's your name?: ")
    question = input("Why do you like programming?: ")
    number_of_people += 1

    with open(file_name, 'a') as f_object:
        f_object.write(f"{name} \n")
        f_object.write(f"{question} \n\n")
