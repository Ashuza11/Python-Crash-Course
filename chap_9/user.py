"""A class that can be used to represent a user"""

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