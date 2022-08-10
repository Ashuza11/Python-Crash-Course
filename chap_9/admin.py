"""
    M. Ashuza 
    Auguest 10 2022
    Python Crash Course Book chapter 9 Exercises 
"""

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


# Question 9-7. Admin

class Admin(Users):
    """Represent a specific kind of user"""
    def __init__(self, first_name, last_name, sex, age):
        """Initialize attributes of parentclass."""
        super().__init__(first_name, last_name, sex, age)
        self.privilages = ["can add post" , "can delete post" , "can ban user"]

    def show_privileges(self):
        """Show a list of privileges"""
        for privilege in self.privilages:
            print("* " + privilege)



admin = Admin("Dan", "Ash", "M", 35)
print("This is the admin privileges: ")
admin.show_privileges()

