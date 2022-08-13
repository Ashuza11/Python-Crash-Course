"""A class that can be used to represent a restaurant"""

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