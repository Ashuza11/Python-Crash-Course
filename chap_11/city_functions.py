"""
    M. Ashuza 
    Auguest 15 2022
    Python Crash Course Book chapter 10 Exercises 
"""
"""A set of classes used to model a country and it's cities"""

def country_city(country_name, city_name, population=''):
    """Return a neatly formated name"""
    if population:
        names = f"{country_name}, {city_name}, - Population {population}"
    else:
        names =  f"{country_name}, {city_name}"
    return names.title()

# names = country_city('Santiago', 'chile', 500000)
# print(names)