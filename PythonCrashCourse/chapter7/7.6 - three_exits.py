'''

Write different versions of either Exercise 7-4 or 7-5 that do
each of the following at least once:
• Use a conditional test in the while statement to stop the loop.
• Use an active variable to control how long the loop runs.
• Use a break statement to exit the loop when the user enters a 'quit' value.
'''


# Use a conditional test in the while statement to stop the loop.

# user_age = 1

# while user_age != 0:
#     user_age = input("What is your age?: ")
#     user_age = int(user_age)

#     if user_age == 0:
#         break
#     elif user_age < 3:
#         print("Since you're 3 years or younger, your ticket is free!")
#     elif user_age <= 12:
#         print("Thank you. Your ticket will cost $10.")
#     elif user_age >= 13:
#         print("Thank you. Your ticket will cost $15.")


#  Use an active variable to control how long the loop runs.

# active = True 

# while active:
    
#     user_age = input("What is your age?: ")
#     user_age = int(user_age)

#     if user_age == 0:
#         active = False
#     elif user_age < 3:
#         print("Since you're 3 years or younger, your ticket is free!")
#     elif user_age <= 12:
#         print("Thank you. Your ticket will cost $10.")
#     elif user_age >= 13:
#         print("Thank you. Your ticket will cost $15.")

# Use a break statement to exit the loop when the user enters a 'quit' value.

while True:

    user_age = input("What is your age?: ")
    user_age = int(user_age)

    if user_age == 0:
        break
    elif user_age < 3:
        print("Since you're 3 years or younger, your ticket is free!")
    elif user_age <= 12:
        print("Thank you. Your ticket will cost $10.")
    elif user_age >= 13:
        print("Thank you. Your ticket will cost $15.")