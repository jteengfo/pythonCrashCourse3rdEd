'''
 Write a while loop that prompts users for their name. Collect
all the names that are entered, and then write these names to a file called
guest_book.txt. Make sure each entry appears on a new line in the file.'''

from pathlib import Path

active = True
response = ''

while active:
    user_response = input("Please enter your name: ")

    if user_response == 'q':
        active = False
    else: 
        response += user_response + '\n'

path = Path('guest_book.txt')
path.write_text(response)

