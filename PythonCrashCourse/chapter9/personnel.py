'''A module that consists the User, Admin, and Privileges classes. '''

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

class Privileges:
    '''A model of a list containing privileges.'''
    def __init__(self, privileges=['can add post', 'can edit post', 'can delete post']):
        '''Initialize attributes.'''
        self.privileges = privileges
    
    def show_privileges(self):
        '''Prints a statment listing all privilege given to the user.'''
        for privilege in self.privileges:
            print(f"\t -{privilege.capitalize()}")

    def add_privileges(self, privileges):
        '''Allows user to add their designated privileges.'''
        self.privileges = privileges


# child class 
class Admin(User):
    '''Model of an admin.'''
    def __init__(self, first_name, last_name, location, age):
        '''Initialize attributes of admin.'''
        super().__init__(first_name, last_name, location, age)
        self.privileges = Privileges()

    # def show_privileges(self):
    #     '''Prints a statment listing all privilege given to the user.'''
    #     print(f"{self.first_name.title()}'s privileges include: ")
    #     for privilege in self.privileges:
    #         print(f"\t -{privilege.capitalize()}")
