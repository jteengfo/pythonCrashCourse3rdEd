# Every Function

'''
Think of things you could sotre in a list. For example, you could make a list of mountains, rivers, countris, cities, languages, oranything youl'd like.
Write a program that creates a list containing these items and then use each function introduced in this chapter at least once
'''

cities = ['Vienna', 'Copenhagen', 'Zurich', 'Calgary', 'Vancouver']

# sorting list temporarily
sorted_cities = sorted(cities)
print(sorted_cities)

# sorting list temporarily but reverse
sorted_cities = sorted(cities, reverse=True)
print(sorted_cities)

# reversing list permanently 
cities.reverse()
print(cities)

# reverse list back to original
cities.reverse()
print(cities)

# sorting list permanently 
cities.sort()
print(cities)

# sorting list permanently but reverse
cities.sort(reverse=True)
print(cities)

# finding the amoung of cities in the list 
cities_num = len(cities)
print(f"The number of cities in the list is {cities_num}.")
