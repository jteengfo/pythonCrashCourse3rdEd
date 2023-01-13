'''
One common problem when prompting for numerical input
occurs when people provide text instead of numbers. When you try to convert
the input to an int, you’ll get a ValueError. Write a program that prompts for
two numbers. Add them together and print the result. Catch the ValueError if
either input value is not a number, and print a friendly error message. Test your
program by entering two numbers and then by entering some text instead of a
number.'''

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
            
    