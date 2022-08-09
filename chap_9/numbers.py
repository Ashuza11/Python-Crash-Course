"""
    M. Ashuza 
    Auguest 02 2022
    Python Crash Course Book chapter 9 Exercises 
"""

# Question 9-4. Number Served
class Restaurant():
    """A simple attemp to model a restaurent"""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and age sttributes"""
        self.name = restaurant_name
        self.cuisine = cuisine_type 
        self.number_served = 10                                                           

    def describe_restaurant(self):
        """Simulate a restaurent in response to a command"""
        name = self.name.title()
        cuisine = self.cuisine.title()
        print(f"Restaurant name: {name}, Restaurant cuisine type: {cuisine}.")

    def open_restaurant(self): 
        """Simulating an open state of the restaurnt"""
        state = "The restaurant" + " " + self.name.title() + " Is opened!"
        print(state)
    
    def set_number_served(self):
        """
            Print a statement showing the number of customers 
            the restaurant has served
        """
        print(f"The restaurant has served {self.number_served} Customers.")

    def increment_number_served(self, served_customers): 
        """Set the number of served customers to a given nuumber"""
        self.number_served = served_customers

restaurant = Restaurant('apetito', 'african')
print(f"The restaurant name is {restaurant.name.title()}.")
print(f"The restaurant Cuisine type is {restaurant.cuisine.title()}.")

restaurant.number_served = 30
restaurant.set_number_served()
restaurant.increment_number_served(40)
print("After only one day we've got 10 new customers!")
restaurant.set_number_served()
restaurant.describe_restaurant()
restaurant.open_restaurant()
print("\n")

# Question 9-5. Login Attempts

class Users():
    """Simulating a user profile"""
    def __init__(self, first_name, last_name, sex, age):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        """Simulating a user profile account"""
        username = self.first_name
        name = self.last_name
        sex = self.sex
        age = self.age
        login = self.login_attempts
        print("User profile Info:"+" " + username.title()+", " + name.title()+", " + sex.title()+", "+ str(age)+ ".")
        print(f"User login {login} times")

    def greet_user(self):
        """Simulating a welcoming user back"""
        username = self.first_name
        print(f"Hello ! {username} thanks and welcome back.")

    def increment_login_attempts(self):
        """Increment the value of login attempts by one"""
        self.login_attempts += 1
           

    def reset_login_attempts(self):
        """Rests the login attempts to 0"""
        self.login_attempts = 0

user1 = Users('ashuza', 'albert', 'm', 19)
user2 = Users('Jomo', 'Kinyata', 'm', 24)

user1.describe_user()
user1.greet_user()
print("\n")
for i in range(1, 4):
    user1.increment_login_attempts()
    user1.describe_user()
user1.reset_login_attempts()
user1.describe_user()


