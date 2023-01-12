''' A class representing a user. '''

# parent class 
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

