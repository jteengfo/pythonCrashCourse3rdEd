'''
Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name.
Store these dictionaries in a list called pets. Next, loop through your list and as
you do, print everything you know about each pet.
'''

pets = []
count = 0

pet1 = {
    'animal' : 'dog',
    'name': 'king',
}
pet2 = {
    'animal' : 'cat',
    'name': 'milo',
}
pet3 = {
    'animal': 'fish',
    'name': 'nemo',
}

pets.append(pet1)
pets.append(pet2)
pets.append(pet3)


for pet in pets:
    count += 1
    petname = pet['name'].title()
    animal = pet['animal'].title()

    print(f"{petname} is a {animal}.")
print(f"Overall, I have {count} pets.")
count = 0