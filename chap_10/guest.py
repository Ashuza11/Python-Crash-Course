"""
    M. Ashuza 
    Auguest 14 2022
    Python Crash Course Book chapter 10 Exercises 
"""
# Question 10-3. Guest

filename = 'guest.txt'

name = input("What's your name?: ")

with open(filename, 'w') as file_obect:
    file_obect.write(f"{name} \n")
    file_obect.write(f"{name} \n")
print("\n")

# Question 10-4. Guest Book
file_name = 'guest_book.txt'
print("Inter q to quit")
active = True
while active:
    name = input("Your name: ")

    if name == 'q':
        active = False
    else:
        print(f"Hello! {name}")

    with open(file_name, 'a') as f_object:
        if name == 'q':
            continue
        f_object.write(f"{name} \n")

print("\n")


