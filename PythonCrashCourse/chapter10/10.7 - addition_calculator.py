'''
Wrap your code from Exercise 10-5 in a while loop
so the user can continue entering numbers, even if they make a mistake and
enter text instead of a number.'''

active = True
while active:
    num1 = input("We are going to add two numbers and will print the result for you. Please enter the first number: ")
    num2 = input("Please enter the second number: ")

    if num1 == 'q' or num2 == 'q':
        active = False
    else: 
        # convert str to int 
        try:
            num1 = int(num1)
            num2 = int(num2)
        except ValueError:
            print("Sorry. One of your inputs is not a number.")

        else:
            sum = num1 + num2 
            print(f"{num1} + {num2} = {sum}")
