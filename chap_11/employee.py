"""
    M. Ashuza 
    Auguest 15 2022
    Python Crash Course Book chapter 10 Exercises 
"""

class Employee():
    """Class to represent an employee."""

    def __init__(self, first_name, last_name, anual_salary):
        """Store employee info details"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.anual_salary = anual_salary
 
    def give_raise(self, raise_amount=5000):
        """Give a raise to employee."""
        self.anual_salary += raise_amount

