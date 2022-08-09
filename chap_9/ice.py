"""
    M. Ashuza 
    Auguest 09 2022
    Python Crash Course Book chapter 9 Exercises 
"""

# Questin Exercise 9-1 
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


# Question 9-6. Ice Cream Stand
class IceCreamStand(Restaurant):
    """Represent a specific kind restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes of the parent class."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['Almond Joy', 'Black Raspberry Chip', 
                    'Bubble Gum', 'Butter Pecan', 'Cherry Vanilla'
                    'Chocolate',   'Vanilla''Chocolate Chip'
                    ]
    def display_ice_list(self):
        """Display a list of ice cream flavors"""
        for flavor in self.flavors:
            print("- " + flavor)

restaurant1 = IceCreamStand('Ice Cream Stand', 'Ice cream')
restaurant1.describe_restaurant()
print("This is the available flavors:")
restaurant1.display_ice_list()


