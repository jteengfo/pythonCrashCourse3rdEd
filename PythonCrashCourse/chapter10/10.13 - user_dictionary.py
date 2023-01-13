'''
The remember_me.py example only stores one piece of
information, the username. Expand this example by asking for two more pieces
of information about the user, then store all the information you collect in a
dictionary. Write this dictionary to a file using json.dumps(), and read it back
in using json.loads(). Print a summary showing exactly what your program
remembers about the user.'''


from pathlib import Path
import json


def get_stored_information(path):
    """Get stored user information if available."""
    if path.exists():
        contents = path.read_text()
        user_info = json.loads(contents)
        return user_info
    else:
        return None

def get_new_information(path):
    """Prompt for a new user info."""
    username = input("What is your name? ")
    location = input('Where do you live? ')
    age = input("What is your age? ")

    # store into a dictionary
    user_info = {
        'username' : username,
        'location' : location,
        'age' : age,
    }

    contents = json.dumps(user_info)
    path.write_text(contents)
    return user_info

def greet_user():
    """Greet the user by name."""
    path = Path('username_dict.json')
    user_info = get_stored_information(path)
    if user_info:
        print(f"Welcome back, {user_info['username']}!")
        print(f"You are {user_info['username'].title()}. You are {user_info['age']} years old and currently residing in {user_info['location'].title()}.")
    else:
        user_info = get_new_information(path)
        print(f"We'll remember you when you come back, {user_info['username'].title()} who is currently {user_info['age']} years old and currently residing in {user_info['location'].title()}!")

greet_user()