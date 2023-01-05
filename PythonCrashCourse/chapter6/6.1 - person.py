'''
Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. You
should have keys such as first_name, last_name, age, and city. Print each piece
of information stored in your dictionary.
'''

bio = {'firstname': 'james',
    'lastname': 'te eng fo',
    'age': 28,
    'city': 'edmonton',}

# print(bio['firstname'].title())
print(bio.get('firstname', 'Sorry, first name unavailable.').title())

print(bio['lastname'].title())

print(bio['age'])

print(bio['city'].title())