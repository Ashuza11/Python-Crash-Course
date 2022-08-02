"""
    M. Ashuza 
    july 29 2022
    Python Crash Course Book chapter 8 Exercises 
"""
# Question 8-9. Magicians

def show_magicians(names):
    """Print a list of name's in a list"""
    print("The magician names are: ")
    for name in names:
        print(name)

magician_names = ['alaba', 'balasha', 'malashe', 'galabe', 'chahca']
show_magicians(magician_names)
print("\n")

# Question 8-10. Great Magicians
def make_great(magician_names, new_magicians):
    """Returns a modified list"""

    items = ''
    phrase = "The Great"
    for i in magician_names:
        items = phrase + ' ' + i
        new_magicians.append(items)
        
    return new_magicians
  
magician_list = ['alaba', 'balasha', 'malashe', 'galabe', 'chahca', 'gabi']
new_magicians = []
modified_magician = make_great(magician_list,  new_magicians)

show_magicians(modified_magician)


print("\n")

# Question 8-11. Unchanged Magicians
print("New name'slist ")
show_magicians(new_magicians)
print("\n")
print("Old name's lsit")
show_magicians(magician_list)