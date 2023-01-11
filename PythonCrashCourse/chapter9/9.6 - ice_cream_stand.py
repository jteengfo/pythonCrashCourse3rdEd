'''
An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class you wrote in
Exercise 9-1 (page 162) or Exercise 9-4 (page 166). Either version of the class
will work; just pick the one you like better. Add an attribute called flavors that
stores a list of ice cream flavors. Write a method that displays these flavors.
Create an instance of IceCreamStand, and call this method.'''

# parent class 
class Restaurant:
    ''' To model a restaurant.'''

    def __init__(self, restaurant_name, cuisine_type):
        '''Initialize restaurant name and cuisine type'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        '''prints out the description of the restaurant'''
        print(f"{self.restaurant_name.title()} is the name of the restaurnt.\nTheir cuisine type is {self.cuisine_type.title()}.")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is now open!")

# child class

class IceCreamStand(Restaurant):
    
    def __init__(self, restaurant_name, cuisine_type='ice cream'):
        ''' Initialize attributes from the parent class.'''
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []
    
    def display_flavors(self):
        ''' Displays all flavors available in the ice cream stand.'''
        flavor_list = self.flavors
        print(f"We have the following flavors: ")
        for flavor in flavor_list:
            print(f"\t- {flavor.title()}")


# creating an instance of an ice cream stand
ice_cream_stand_1 = IceCreamStand('dinkin')
ice_cream_stand_1.flavors = ['chocolate', 'vanilla', 'death by chocolate', 'matcha']
ice_cream_stand_1.display_flavors()