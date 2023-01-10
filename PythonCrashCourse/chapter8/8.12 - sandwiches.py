'''
Write a function that accepts a list of items a person wants
on a sandwich. The function should have one parameter that collects as many
items as the function call provides, and it should print a summary of the sandwich that’s being ordered. Call the function three times, using a different number of arguments each time.'''

def build_sandwich(*ingredients):
    print(f"Building a sandwich consisting of:")
    for ingredient in ingredients:
        print(f"- {ingredient}")

build_sandwich('bun')

build_sandwich('bun', 'ketchup', 'mustard')

build_sandwich('bun', 'ketchup', 'mustard', 'onions', 'beef patty', 'cheese')