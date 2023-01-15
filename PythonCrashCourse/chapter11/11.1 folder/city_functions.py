# def city_country(city, country):
#     '''A function that returns the string City, Country'''
#     city = city.title()
#     country = country.title()
#     string = f"{city}, {country}"
#     return string

def city_country(city, country, population=''):
    '''A function that returns the string City, Country'''

    if population:
        city = city.title()
        country = country.title()
        string = f"{city}, {country} - population: {population}"
        return string
    else:
        city = city.title()
        country = country.title()
        string = f"{city}, {country}"
        return string

