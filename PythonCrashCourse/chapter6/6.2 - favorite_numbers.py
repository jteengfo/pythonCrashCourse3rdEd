'''
: Use a dictionary to store people’s favorite numbers.
Think of five names, and use them as keys in your dictionary. Think of a favorite
number for each person, and store each as a value in your dictionary. Print
each person’s name and their favorite number. For even more fun, poll a few
friends and get some actual data for your program.
'''

favorite_numers = {
    'james': 8,
    'john': 7,
    'amy': 13,
    'emma': 28,
    'avery': 69,
}

for key in favorite_numers:
    name = key
    print(f"{name.title()}'s favorite number is {favorite_numers[key]}")