'''Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.
Create several instances representing different users, and call both methods for each user.'''

class User:
    '''Model of a user'''

    def __init__(self, first_name, last_name, location, age):
        '''Initialize first_name and last_name attributes'''
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.age = age

    def describe_user(self):
        print(f"User's name is {self.first_name.title()} {self.last_name.title()}. User is currently {self.age} years old and currently resides in {self.location.title()}.\n")

    def greet_user(self):
        print(f"Hello {self.first_name.title()}!")


user_1 = User('james', 'te eng fo', 'edmonton', 28)
user_2 = User('anise', 'cooper', 'nunavut', 39)
user_3 = User('lancelot', 'princeton', 'mars', 74)

user_list = [user_1, user_2, user_3]

for user in user_list:
    user.describe_user()
    user.greet_user()