'''Write a program that prompts for the user’s favorite
number. Use json.dumps() to store this number in a file. Write a separate program that reads in this value and prints the message “I know your favorite
number! It’s _____.”'''

from pathlib import Path
import json

# prompt user for their fav number
favorite_number = input("What is your favorite number?: ")

# store favorite number into json format (string)
content = json.dumps(favorite_number)

# write the json formatted string version of the favorite number to a text file
path = Path('favorite_number.txt')
path.write_text(content)


content = path.read_text()
favorite_number_read = json.loads(content)
print(f"I know your favorite number! It is {favorite_number_read}!")

