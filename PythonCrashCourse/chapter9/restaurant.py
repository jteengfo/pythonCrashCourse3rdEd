''' A class that represents a Restaurant.'''

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
