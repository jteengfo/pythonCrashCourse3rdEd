'''
Add an attribute called login_attempts to your User class
from Exercise 9-3 (page 162). Write a method called increment_login_attempts()
that increments the value of login_attempts by 1. Write another method called
reset_login_attempts() that resets the value of login_attempts to 0.
Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts(). Print login_attempts again to
make sure it was reset to 0.'''

class User:
    '''Model of a user'''

    def __init__(self, first_name, last_name, location, age):
        '''Initialize first_name and last_name attributes'''
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        '''describes the user using all information attributed to the user.'''
        print(f"User's name is {self.first_name.title()} {self.last_name.title()}. User is currently {self.age} years old and currently resides in {self.location.title()}.\n")

    def greet_user(self):
        '''prints a greeting towards the user.'''
        print(f"Hello {self.first_name.title()}!")

    def increment_login_attempts(self):
        '''increments the number of user login attempts by 1.'''
        self.login_attempts += 1

    def reset_login_attempts(self):
        '''resets the amount of user login attemtps back to 0.'''
        self.login_attempts = 0

user_1 = User('james', 'te eng fo', 'edmonton', 28)

user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()

print(f"{user_1.first_name.title()} has attempted to login for a total number of {user_1.login_attempts} tries.")
user_1.reset_login_attempts()

print(f"{user_1.first_name.title()}'s total number of login attemtps has been resetted. it is now back to {user_1.login_attempts}.")