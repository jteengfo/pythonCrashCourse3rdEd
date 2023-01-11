'''
Start with your class from Exercise 9-1. Create three
different instances from the class, and call describe_restaurant() for each
instance.'''


class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        '''Initialize restaurant name and cuisine type'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        '''prints out the description of the restaurant'''
        print(f"{self.restaurant_name.title()} is the name of the restaurnt.\nTheir cuisine type is {self.cuisine_type.title()}.\n")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is now open!\n")

restaurant_1 = Restaurant('good buddy','chinese cuisine')
restaurant_2 = Restaurant("it'dog", 'corndogs and chicken')
restaurant_3 = Restaurant("hanjan", "korean cuisine")


restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()