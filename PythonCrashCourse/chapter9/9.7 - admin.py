'''
An administrator is a special kind of user. Write a class called Admin that inherits from the User class you wrote in 
Exercise 9-3 (page 162) or Exercise 9-5 (page 167). Add an attribute, privileges, 
that stores a list of strings like "can add post", "can delete post", "can ban user", and so on. 
Write a method called show_privileges() that lists the administrator’s set of privileges. 
Create an instance of Admin, and call your method.'''

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


class Admin(User):
    '''Model of an admin.'''
    def __init__(self, first_name, last_name, location, age):
        '''Initialize attributes of admin.'''
        super().__init__(first_name, last_name, location, age)
        self.privileges = []

    # def show_privileges(self):
    #     '''Prints a statment listing all privilege given to the user.'''
    #     print(f"{self.first_name.title()}'s privileges include: ")
    #     for privilege in self.privileges:
    #         print(f"\t -{privilege.capitalize()}")

admin_1 = Admin('john','doe','edmonton','29')
admin_1.privileges = ['can add post', 'can edit post', 'can delete post']

admin_1.show_privileges()