'''
: Make a list containing a series of short text messages. Pass the
list to a function called show_messages(), which prints each text message.'''


short_messages = [
    'hello! I am Jarvis!',
    'I am optimus prime!',
    "Hi, we've been trying to reach you about your car's extended warranty'",
]


def show_messages(messages):
    for message in messages:
        print(f"{message.capitalize()}")

show_messages(short_messages)