'''
Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.
Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.
'''

class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        '''Initialize restaurant name and cuisine type'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        '''prints out the description of the restaurant'''
        print(f"{self.restaurant_name.title()} is the name of the restaurnt.\nTheir cuisine type is {self.cuisine_type.title()}.")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is now open!")


restaurant_1 = Restaurant('good buddy','chinese cuisine')

print("Restaurant's name is Good Buddy")
print("\nIts cuisine type is chinese cuisine.")

restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()