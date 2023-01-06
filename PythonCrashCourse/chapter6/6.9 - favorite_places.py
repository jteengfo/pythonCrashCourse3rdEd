'''
: Make a dictionary called favorite_places. Think of three
names to use as keys in the dictionary, and store one to three favorite places for
each person. To make this exercise a bit more interesting, ask some friends to
name a few of their favorite places. Loop through the dictionary, and print each
person’s name and their favorite places.
'''

favorite_places = {
    'james': {'home', 'apri', 'indigo',},
    'myke' : {'home', "parent's house in the states", 'with my friends',},
    'daniel' : {'home', 'japan', 'france',},
    'cath': {},
    'crystal': {},
    'julia': {'home', 'home', 'home',},
}

for key, value in favorite_places.items():
    name = key.title()
    print(f"\n{name}'s three favorite places are:")
    for favorite_place in value:
        print(f"\t{favorite_place.capitalize()}")