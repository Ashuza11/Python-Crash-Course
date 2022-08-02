"""
    M. Ashuza 
    Auguest 02 2022
    Python Crash Course Book chapter 8 Exercises 
"""
# Question 8-13. User Profile
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    
    profile['first_name'] = first
    profile['last_name'] = last
    
    for key, value in user_info.items():
        profile[key] = value
    return profile

# Question 8-14. Cars
def make_car(manufacturer, model_name, **other_info):
    """Build a dictionary containing everything we know about a car."""
    car_info = {}

    car_info['manufacturer_name'] = manufacturer
    car_info['model_name'] = model_name

    for key, value in other_info.items():
        car_info[key] = value
    return car_info

car = make_car('subaru', 'outback', color='blue', tow_package=True)

print(car)