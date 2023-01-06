'''
Write a program that asks the user how many people
are in their dinner group. If the answer is more than eight, print a message saying they’ll have to wait for a table. Otherwise, report that their table is ready

'''

user_input = input("How many people do you in your dinner group?: ")

# str > int conversion
user_input = int(user_input)

if user_input > 8:
    print("With the dinner group size that you have, unfortunately you will to wait for a table. Apologies.")
else:
    print("Great. Your table is ready. Come follow me.")
