'''
Start with your program from Exercise 9-1 (page 162).
Add an attribute called number_served with a default value of 0. Create an
instance called restaurant from this class. Print the number of customers the
restaurant has served, and then change this value and print it again.

Add a method called set_number_served() that lets you set the number of
customers that have been served. Call this method with a new number and print
the value again.

Add a method called increment_number_served() that lets you increment
the number of customers who’ve been served. Call this method with any number
you like that could represent how many customers were served in, say, a day of
business.
'''

class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        '''Initialize restaurant name and cuisine type'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        '''prints out the description of the restaurant'''
        print(f"{self.restaurant_name.title()} is the name of the restaurnt.\nTheir cuisine type is {self.cuisine_type.title()}. It currently has served {self.number_served} customers.")
    
    def open_restaurant(self):
        '''prints a notice that the restaurant is now open.'''
        print(f"{self.restaurant_name.title()} is now open!")
    
    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, number_served):
        self.number_served += number_served



restaurant_1 = Restaurant('good buddy','chinese cuisine')

restaurant_1.describe_restaurant()
# directly setting number_served value to 1.
restaurant_1.number_served = 1
restaurant_1.describe_restaurant()

restaurant_1.set_number_served(3)
restaurant_1.describe_restaurant()

restaurant_1.increment_number_served(5)
restaurant_1.describe_restaurant()