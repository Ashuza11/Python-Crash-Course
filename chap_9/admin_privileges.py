""""A class that can be used to represent an admin and his privileges"""
from user import Users

class Privileges():
    """Represent the admin's privileges"""
    def __init__(self):
        self.privileges = ["can add post" , "can delete post" , "can ban user"]

    def show_privileges(self):
        """Show a list of privileges"""
        for privilege in self.privileges:
            print("* " + privilege)


# Question 9-7. Admin

class Admin(Users):
    """Represent a specific kind of user"""
    def __init__(self, first_name, last_name, sex, age):
        """Initialize attributes of parentclass."""
        super().__init__(first_name, last_name, sex, age)
        self.email = "dan@gmail.com"
        self.privilege = Privileges()