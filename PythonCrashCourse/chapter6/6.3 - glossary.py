'''
A Python dictionary can be used to model an actual dictionary.
However, to avoid confusion, let’s call it a glossary.
• Think of five programming words you’ve learned about in the previous
chapters. Use these words as the keys in your glossary, and store their
meanings as values.
• Print each word and its meaning as neatly formatted output. You might
print the word followed by a colon and then its meaning, or print the word
on one line and then print its meaning indented on a second line. Use the
newline character (\n) to insert a blank line between each word-meaning
pair in your output.
'''

glossary = {
    'string' : 'a series of characters stored as a words', 
    'list' : 'a container that is dynamic and unorderd that can store objects', 
    'for loop' : 'an itervative statement used to check certain conditions repeatedly.', 
    'dictionary' : 'a container, similar to list, that can store key-value pairs and values accessed through keys', 
    'key': 'a analogous to index of a list. It is used to access values that are associated with their respective keys '
}

for key, value in glossary.items():
    print(f"{key.title()} is {value}")
