'''
Write a loop that prompts the user to enter a series of
pizza toppings until they enter a 'quit' value. As they enter each topping, print
a message saying you’ll add that topping to their pizza.
'''

message = ""

while message != 'quit':
    message = input("Please enter a pizza topping: ")

    if message != 'quit':
        print(f"Adding {message} toppings to the pizza.")
