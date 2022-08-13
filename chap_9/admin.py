"""
    M. Ashuza 
    Auguest 10 2022
    Python Crash Course Book chapter 9 Exercises 
"""

# Question 9-5. Login Attempts
import email


class Users():
    """Simulating a user profile"""
    def __init__(self, first_name, last_name, sex, age):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age
        self.email = 'dan@ashec.com'
        self.login_attempts = 0

    def describe_user(self):
        """Simulating a user profile account"""
        username = self.first_name
        name = self.last_name
        sex = self.sex
        age = self.age
        login = self.login_attempts
        email = self.email
        print("User profile Info:"+" " + username.title()+", " + name.title()+", " + sex.title()+", "+ str(age) +" "+ email + ".")
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


# Question 9-8. Privileges: 
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


admin = Admin("Dan", "Ash", "M", 35)
admin.describe_user()
print("This is the admin privileges: ")
admin.privilege.show_privileges()





# 9-8. Privileges: Write a separate Privileges class. The class should have one
# attribute, privileges , that stores a list of strings as described in Exercise 9-7.
# Move the show_privileges() method to this class. Make a Privileges instance
# as an attribute in the Admin class. Create a new instance of Admin and use your
# method to show its privileges.