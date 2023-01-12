''' A moodule that contains the Admin, and Privileges class. '''

from user import User

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