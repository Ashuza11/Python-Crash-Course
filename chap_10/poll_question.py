"""A class that can be used to represent a poll"""

class Poll():
    """A simple attempte to represent a poll"""
    def __init__(self, first_name, last_name, age, question):
        """Initialize atributes to discribe a poll"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.question = question
        self.responding_people = 0

    def questionaire(self):
        """Represent a poll questionaire"""
        while self.responding_people < 5:
            self.first_name = input("Your first name: ")
            self.last_name = input("Your last name: ")
            self.age = input("How old are you?: ")
            self.question = input("Why do you like programming?: ")
            print("Thank you for taking the poll.")
            self.responding_people += 1

    def store_poll_data(self):
        """Store the poll data in a file"""
