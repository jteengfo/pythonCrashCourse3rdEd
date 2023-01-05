'''
Now that you know how to loop through a dictionary, clean
up the code from Exercise 6-3 (page 99) by replacing your series of print()
calls with a loop that runs through the dictionary’s keys and values. When
you’re sure that your loop works, add five more Python terms to your glossary.
When you run your program again, these new words and meanings should
automatically be included in the output.

'''

glossary = {
    'string' : 'a series of characters stored as a words', 
    'list' : 'a container that is dynamic and unorderd that can store objects', 
    'for loop' : 'an itervative statement used to check certain conditions repeatedly.', 
    'dictionary' : 'a container, similar to list, that can store key-value pairs and values accessed through keys', 
    'key': 'a analogous to index of a list. It is used to access values that are associated with their respective keys ',
    'set' : 'a container used to store multiple items in a single variable and are unordered', 'variable' : 'a container for storing data values', 'print()' : 'is a function that prints a message onto the screen', 'sorted()' : 'is a function that returns a sorted list of the specified iterable object', 'python' : 'is an interpreted programming language.'
}

for key, value in glossary.items():
    print(f"{key.title()} is {value}")
