'''
 Make a dictionary called cities. Use the names of three cities as
keys in your dictionary. Create a dictionary of information about each city and
include the country that the city is in, its approximate population, and one fact
about that city. The keys for each city’s dictionary should be something like
country, population, and fact. Print the name of each city and all of the information you have stored about it.
'''

cities_dict = {
    'edmonton' : {
        'country' : 'canada',
        'population': 1519000,
        'fact': "Edmonton's River Valley is 22 times the size of New York's Central Park",
    },
    'calgary' : {
        'country' : 'canada',
        'population': 1611000,
        'fact': "Calgary is one of the youngest cities in Canada with an average age of 3",
    },
    'toronto' : {
        'country' : 'canada',
        'population': 6313000,
        'fact':"Toronto has over 10 million trees",
    },
}

for key, value in cities_dict.items():
    cityname = key.title()
    print(f"\nThis is the city of {cityname}.")
    for info in value:
        countryname = value['country'].title()
        population = value['population']
        fact = value['fact'].capitalize()

    print(f"{cityname} is a city from {countryname}. It has about {population} amount of people in it as of 2022. Fun fact, {fact}.")
