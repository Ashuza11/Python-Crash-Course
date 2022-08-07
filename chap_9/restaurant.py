"""
    M. Ashuza 
    Auguest 02 2022
    Python Crash Course Book chapter 9 Exercises 
"""

# Question 9-1. Restaurant


class Restaurant():
    """A simple attemp to model a restaurent"""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and age sttributes"""
        self.name = restaurant_name
        self.cuisine = cuisine_type                                                               

    def describe_restaurant(self):
        """Simulate a restaurent in response to a command"""
        name = self.name.title()
        cuisine = self.cuisine.title()
        print(f"Restaurant name: {name}, Restaurant cuisine type: {cuisine}.")

    def open_restaurant(self): 
        """Simulating an open state of the restaurnt"""
        state = "The restaurant" + " " + self.name.title() + " Is opened!"
        print(state)


restaurant = Restaurant('apetito', 'african')
print(f"The restaurant name is {restaurant.name.title()}.")
print(f"The restaurant Cuisine type is {restaurant.cuisine.title()}.")

restaurant.describe_restaurant()
restaurant.open_restaurant()
print("\n")

# Question 9-2. Three Restaurants
restaurant1 = Restaurant('Manishe', 'Congolese')
restaurant1.describe_restaurant()
restaurant2 = Restaurant('Malewa', 'Chinees')
restaurant2.describe_restaurant()
restaurant3 = Restaurant('chaba', 'Rwandeese')
restaurant3.describe_restaurant()
print("\n")

# Question 9-3. Users:
class Users():
    """Simulating a user profile"""
    def __init__(self, first_name, last_name, sex, age):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age

    def describe_user(self):
        """Simulating a user profile account"""
        username = self.first_name
        name = self.last_name
        sex = self.sex
        age = self.age
        print("User profile Info:"+" " + username.title()+", " + name.title()+", " + sex.title()+", "+ str(age)+ ".")

    def greet_user(self):
        """Simulating a welcoming user back"""
        username = self.first_name
        print(f"Hello ! {username} thanks and welcome back.")

user1 = Users('ashuza', 'albert', 'm', 19)
user1 = Users('Jomo', 'Kinyata', 'm', 24)
user1 = Users('Aline', 'mwinja', 'f', 22)

user1.describe_user()
user1.greet_user()

