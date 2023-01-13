'''Combine the two programs you wrote in
Exercise 10-11 into one file. If the number is already stored, report the favorite
number to the user. If not, prompt for the user’s favorite number and store it in a
file. Run the program twice to see that it works.'''

from pathlib import Path
import json
path = Path('favorite_number.txt')


if path.exists():
    path = Path('favorite_number.txt')
    content = path.read_text()
    favorite_number_read = json.loads(content)
    print(f"I know your favorite number! It is {favorite_number_read}!")

else:
    # prompt user for their fav number
    favorite_number = input("What is your favorite number?: ")

    # store favorite number into json format (string)
    content = json.dumps(favorite_number)

    # write the json formatted string version of the favorite number to a text file
    path.write_text(content)

