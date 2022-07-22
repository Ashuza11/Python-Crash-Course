# Question 5-8. Hello Admin 
import numbers


usernames = []

for username in usernames:
    if username == 'admin':
        print(f"Hello {username}, would you like to see a status report?")
    if username:
        print("Hello user we love!")
    
# Question 5-9. No Users
if usernames == []:
    print("We need to find some users!")
print("\n")

# Question 5-10. Checking Usernames

# Make a list of five or more usernames called current_users .
current_users = ['alse', 'david', 'ben', 'arnold', 'yves', 'freddi', 'jomo']
# • Make another list of five usernames called new_users . Make sure one or
new_users = ['binet', 'bill', 'Ben', 'David', 'ines']
# two of the new usernames are also in the current_users list.
# • Loop through the new_users list to see if each new username has already
for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"The username {new_user.title()} has been user pease! inter a new username.")
    else:
        print(f"The username is avalable.")
# been used. If it has, print a message that the person will need to enter a
# new username. If a username has not been used, print a message saying
# that the username is available.
# Make sure your comparison is case insensitive. If 'John' has been used,
# 'JOHN' should not be accepted.



# Question 5-11. Ordinal Numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 2:
        print(f"{number}rd")
    elif number == 3:
        print(f"{number}th")
    elif number == 5:
        print(f"{number}th")
    elif number == 6:
        print(f"{number}th")
    elif number == 7:
        print(f"{number}th")
    elif number == 8:
        print(f"{number}th")
    else:
        print(f"{number}th")
# Store the numbers 1 through 9 in a list.
# • Loop through the list.
# • Use an if - elif - else chain inside the loop to print the proper ordinal end-
# ing for each number. Your output should read "1st 2nd 3rd 4th 5th 6th
# 7th 8th 9th" , and each result should be on a separate line.