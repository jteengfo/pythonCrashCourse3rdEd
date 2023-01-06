'''

A movie theater charges different ticket prices depending on
a person’s age. If a person is under the age of 3, the ticket is free; if they are
between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
$15. Write a loop in which you ask users their age, and then tell them the cost
of their movie ticket.

'''

user_age = 1

while user_age != 0:
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

    