'''
Modify your except block in Exercise 10-7 to fail
silently if either file is missing.'''

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
            # print("Sorry. One of your inputs is not a number.")
            pass

        else:
            sum = num1 + num2 
            print(f"{num1} + {num2} = {sum}")
