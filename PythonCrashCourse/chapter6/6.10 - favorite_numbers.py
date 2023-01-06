'''

Modify your program from Exercise 6-2 (page 98) so
each person can have more than one favorite number. Then print each person’s
name along with their favorite numbers.
'''

favorite_numers = {
    'james': [8, 3, 13],
    'john': [7, 8, 9],
    'amy': [13, 21, 26],
    'emma': [28, 27, 30],
    'avery': [69, 420, 3.14],
}

for key, list in favorite_numers.items():
    name = key.title()
    print(f"\n{name}'s favorite numbers are:")
    for number in list:
        print(f"\t{number}")