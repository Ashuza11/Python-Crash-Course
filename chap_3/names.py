"""
    M. Ashuza 
    july 1 2022
    Python Crash Course Book chapter 3 Exrcises 
"""
# Question1 3-1. Names
my_freinds_name = ['David', 'Jomo', 'Jedeon', 'Alse']
print(my_freinds_name[0])
print(my_freinds_name[1])
print(my_freinds_name[2])
print(my_freinds_name[3])

# Question2 3-2. Greetings

print(f"\nHey, {my_freinds_name[0]} how are you doing?")
print(f"Hey, {my_freinds_name[1]} how are you doing?")
print(f"Hey, {my_freinds_name[2]} how are you doing?")
print(f"Hey, {my_freinds_name[3]} how are you doing?\n")

# Quesrion3 3-3. Your Own List
bysicles = ['trek', 'cannondale', 'redline', 'specialized']
print(f"I would like to own {bysicles[0]} motorcycle")

# Question4 3-4. Guest List 
my_guests = ['alse', 'emma', 'David']
print(f"Hey, {my_guests[0]} I would like to invite you to denner")
print(f"Hey, {my_guests[1]} I would like to invite you to denner")
print(f"Hey, {my_guests[2]} I would like to invite you to denner\n")

# Question5 3-5. Changing Guest List
print(f"Hello, {my_guests[1]} I am really sorry to heare that my be next time!\n")
my_guests[1]  = "Jomo"
for guest in my_guests:
    print(f"Hey, {guest} I would like to invite you to denner once more again.\n")


# Question6 3-6. More Guests
print(f"Hello guys, haha ! i am happy i found a bigger table, so there is more room available.")
my_guests.insert(0, "Alain") 
my_guests.insert(2, "Ben") 
my_guests.append("Arnold") 
for guest in my_guests:
    print(f"Hey, {guest} I'm more than happy to invite you to denner with me to night.\n")

# Question7 3-7. Shrinking Guest List
print(f"Hello guys, I am really sorry the dinner table won't be available on time there's only space for two people.\n")
for guest in my_guests[:4]:
    guest_removed = my_guests.pop()
    print(f"Hello, {guest_removed} i am really sorry I can't Ivite you to dinner enymore there's only a space for two people.\n")

# With list comprehension 
my_remaning_guest = [print(f"Hello, {guest} you're still invited") for guest in my_guests]

print(f"Hello, {my_guests[0]} you're still invited") 
print(f"Hello, {my_guests[1]} you're still invited\n") 

del my_guests[1]
print(my_guests)
del my_guests[0]
print(f"Hello, {my_guests} I dont need eny guest.\n") 

# Question8 3-8. Seeing the World
my_to_visite_placies = ['Us', 'Ukrein', 'Chine', 'Australi', 'Canada', 'Corea', 'Japan']

print(f"My to visite countries are {my_to_visite_placies}")

print(f"My to visite countries in alphabetical order {sorted(my_to_visite_placies)}")
print(f"My to visite countries are {my_to_visite_placies}\n") # sorted doen't change the list 
# My list in reverse order 

print(f"My to visite countries in alphabetical order {sorted(my_to_visite_placies, reverse=True) }")
print(f"My to visite countries are {my_to_visite_placies}\n") # sorted doen't change the list 

my_to_visite_placies.reverse()
print(f"My to visite countries reversed are {my_to_visite_placies}\n") # reverse the list changes
my_to_visite_placies.reverse()
print(f"My to visite countries reversed are {my_to_visite_placies}\n") # reverse the list changes

my_to_visite_placies.sort()
print(f"My to visite countries reversed are {my_to_visite_placies}\n") # sorte the ist

my_to_visite_placies.sort(reverse=True)
print(f"My to visite countries reversed are {my_to_visite_placies}\n") # sorte the ist

# Question9 3-9. Dinner Guests

print(f"The number of my freinds i invite to dinner with me is {len(my_freinds_name)}\n")

# Question10 3-10. Every Function
my_favorite_languagies = []

my_favorite_languagies.append("English")
my_favorite_languagies.append("Franch")
my_favorite_languagies.append("Kiswahili")
my_favorite_languagies.append("Lingala")
my_favorite_languagies.append("Spanish")

print(f"My favrite languages are {my_favorite_languagies}\n") 
print(f"My to visite countries in alphabetical order {sorted(my_favorite_languagies)}")
print(f"My to visite countries in alphabetical order {sorted(my_favorite_languagies, reverse=True)}")

my_favorite_languagies.sort()
print(f"My favrite languages are {my_favorite_languagies}\n") 

my_favorite_languagies.sort(reverse=True)
print(f"My favrite languages are {my_favorite_languagies}\n") 

print(f"I like  {len(my_favorite_languagies)} Languagies\n") 