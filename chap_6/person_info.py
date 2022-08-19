"""
    M. Ashuza 
    july 22 2022
    Python Crash Course Book chapter 6 Exercises 
"""
# # Question 6-1. Person
# persons_info = {'first_name': 'Mwendelwa', 'last_name': 'David', 'age': 20, 'city': 'Goma'}
# print(persons_info)
# for k, v in persons_info.items():
#     print(k+':', v)
# print("\n") 

# # Question 6-2. Favorite Numbers

# favorite_numbers = {'Alse': 3, 'Jomo': 4, 'yves': 2, 'Hugette': 6, 'Chrispin': 7}
# for k, v in favorite_numbers.items():
#     print(k+':'+' is number', v)
# print("\n")

# Question 6-3. Glossary
glossary = {'variable': 'A name which holds a value', 'function': 'A block of code for doing a given task', 'list': 'A data type which can holds many values'}

print(f" A varaible is {glossary['variable']}")
print(f" A function is {glossary['function']}")
print(f" A list is {glossary['list']}")


print("\n")
# Question 6-4. Glossary 2
for k, v in glossary.items():
    print(k.title()+':', v +'\n')
print("\n")

# Question 6-5. Rivers
rivers = {'nil': 'egypt', 'river congo': 'DR Congo', 'Tanganyika': 'DR Congo'}
# Use a loop to print a sentence about each river, such as The Nile runs
# through Egypt.
for k, v in rivers.items():
    print(k.title()+' runs hrough ', v +'\n')
print("\n")
# • Use a loop to print the name of each river included in the dictionary.
print("The names of each reaver are:")
for k in rivers.keys():
    print(k)
print("\n")
# • Use a loop to print the name of each country included in the dictionary.
print("The names of each country are:")
for values in rivers.values():
    print(values)
print("\n")
# Question 6-6. Polling

# Make a list of people who should take the favorite languages poll. Include
# some names that are already in the dictionary and some that are not.
polling = {
        'Alse': 'c', 
        'Jomo': 'python', 
        'yves': 'java', 
        'Hugette': 'php', 
        'Chrispin': 'javascript'
        }

for k, v in polling.items():
    print(f"{k.title()}'s favorite language is {v}.")
print("\n")

programmers = ['Alse', 'Jomo', 'yves', 'Hugette', 'Chrispin', 'alice', 'Daniel', 'Michelle']

for programmer in programmers:
    if programmer not in polling.keys():
        print(f"{programmer.title()} What's your favorite Programming language please!")
    else:
        print(f"{programmer.title()} Thanks for taking the poll.")
print("\n")


# Question 6-7. People
people = []
person1 = {
        'name': 'David', 
        'programming_laguage': 'python', 
        'level': 'senior', 
        'age': 20, 
        }
people.append(person1)

person2 = {
        'name': 'Germin', 
        'programming_laguage': 'c#', 
        'level': 'Junier', 
        'age': 25, 
        }
people.append(person2)

person3 = {
        'name': 'Ben', 
        'programming_laguage': 'c++', 
        'level': 'Junier', 
        'age': 26, 
        }
people.append(person3)

for person in people:
    name_progamming_laguage = person['name'].title() + " is a " + person['programming_laguage'].title()
    Level = person['level'].title()
    age = int(person['age'])

    print(f"{name_progamming_laguage} {Level} Developer he's {age}.")
print("\n")

# Question 6-8. People
pets = []

pet = {'type': 'dog', 'name': 'bolbol', 'owner': 'Dan', 'wieght': 20}
pets.append(pet)

pet = {'type': 'cheken', 'name': 'kuku', 'owner': 'Ben', 'wieght': 10}
pets.append(pet)

pet = {'type': 'dog', 'name': 'boal', 'owner': 'jemen', 'wieght': 15}
pets.append(pet)

pet = {'type': 'rabbit', 'name': 'zebla', 'owner': 'aline', 'wieght': 10}
pets.append(pet)
for pet in pets:
    print(f"\n * Here's what i know about {pet['name'].title()}:")
    for k, v in pet.items():
        print(k + " :",str(v))
print("\n")

# Question 6-9. Favorite Places
favorite_placies = {
        'ash': ['goma', 'beni', 'butembo'],
        'aline': ['uvira', 'bukavu', 'lubumbashi'],
        'alain': ['kigali', 'bujumbura', 'kampala', 'nairobi']
}

for names, placies in favorite_placies.items():
    print(f"{names.title()} Likes the folowing places:")
    for place in placies:
        print('- ' + place.title())
    print("\n")


# Question 6-10. Favorite Numbers 
favorite_numbers = {
            'Alse': [3, 4, 5, 63, 56, 78], 
            'Jomo': [3, 3, 5, 93, 56, 78],
            'yves': [3, 4, 9, 63, 56, 78],
            'Hugette': [3, 6, 5, 63, 56, 78],
            'Chrispin': [3, 4, 3, 63, 56, 78]
            }
for names, numbers in favorite_numbers.items():
    print(f"{names.title()} Likes the folowing numbers:")
    for number in numbers:
        print('* ' + str(number))
    print("\n")

# Question 6-11. Cities

cities = {
        'goma': {
            'Country': 'dr congo',
            'population': 80000,
            'fact': 'touristique city'
        },
        
        'bukavu': {
            'country': 'dr congo',
            'poppulation': 70000,
            'fact': 'commical city'
        }
}

for names, caracteristics in cities.items():
    print(f"{names.title()} Has the folowing caracteristics: ")
    for k, v in caracteristics.items():
        print(f"{k.title()} : {str(v).title()}")
    print("\n")

# Quesrion 6-12. Extensions
