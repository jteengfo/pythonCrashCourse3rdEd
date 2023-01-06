'''
Ask the user for a number, and then report whether the
number is a multiple of 10 or not.

'''

user_input = input("Please enter a number: ")

# str > int 
user_input = int(user_input)

if user_input % 2 == 0:
    print(f"Nice! {user_input} is a multiple of 10!")
else:
    print(f"Bummer. {user_input} is not a multiple of 10 unfortunately.")