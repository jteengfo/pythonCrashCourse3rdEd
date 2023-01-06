'''
Start with the program you wrote for Exercise 6-1 (page 98). Make
two new dictionaries representing different people, and store all three dictionaries in a list called people. Loop through your list of people. As you loop through
the list, print everything you know about each person
'''

person1 = {'firstname': 'james',
    'lastname': 'te eng fo',
    'age': 28,
    'city': 'edmonton',}

person2 = {'firstname': 'nemi',
    'lastname': 'jackson',
    'age': 25,
    'city': 'calgary',}

person3 = {'firstname': 'joanne',
    'lastname': 'prince',
    'age': 31,
    'city': 'vancouver',}

persons = [person1, person2, person3]

for person in persons:
    firstname = person['firstname'].title()
    lastname = person['lastname'].title()
    age = person['age']
    city = person['city'].title()

    print(f"\nFirst Name: {firstname}")
    print(f"Last Name: {lastname}")
    print(f"Age: {age}")
    print(f"City: {city}")

# # print(bio['firstname'].title())
# print(bio.get('firstname', 'Sorry, first name unavailable.').title())

# print(bio['lastname'].title())

# print(bio['age'])

# print(bio['city'].title())

