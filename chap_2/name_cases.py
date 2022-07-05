"""
    M. Ashuza 
    july 1 2022
    Python Crash Course Book chapter 2 Exrcises 
"""

# Question1 2-3. Personal Message

name = "Eric"
print("\tHello" + " " + name + " "  "would you like to learn some Python today" + "?")
print(f"Hello {name} would you like to learn some Python today?\n")

# Question2 2-4. Name Cases

name_case = "ashuza"
name_titled = name_case.title()
print(f"Hello {name_titled} would you like to learn some Python today?")
name_upper_case = name_case.upper()
print(f"Hello {name_upper_case} would you like to learn some Python today?")
name_lower_case = name_case.lower()
print(f"Hello {name_lower_case} would you like to learn some Python today?\n")

# Question3  Famous quote
print('Albert Einstein once said, "A person who never made amistake never tried anything new."\n')

# Question4 2-5 Famous quote 2

famous_person = "Albert Einstein"
message = "“A person who never made a mistake never tried anything new.”"
print(f"{famous_person} once said, {message}\n")

# Question5 Stripping Names

name_space =  " ashuza " 
print(f"\t{name_case}\n")
remove_right_space = name_space.rstrip()
print(f"\t{remove_right_space}\n")
remove_left_space = name_space.lstrip()
print(f"\t{remove_left_space}\n")
remove_both_spaces = name_space.strip()
print(f"\t{remove_both_spaces}\n")

# Questin6 Number Eight

print(3 + 5)
print(10 - 2)
print(16 / 2)
print(4 * 2)

# Question7 Favorite Number

my_favorite_number = 5
print(f"\t My Favorite number is {str(my_favorite_number)}.")

# Question8 Adding Comments
# Already done 