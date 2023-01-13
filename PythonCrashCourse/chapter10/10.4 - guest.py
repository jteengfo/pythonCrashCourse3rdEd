''''
Write a program that prompts the user for their name. When they
respond, write their name to a file called guest.txt.'''

from pathlib import Path

user_response = input("Hello, please enter your name: ")

path = Path('guest.txt')
path.write_text(user_response)

