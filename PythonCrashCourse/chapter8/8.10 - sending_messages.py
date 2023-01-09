'''
Start with a copy of your program from Exercise 8-9.
Write a function called send_messages() that prints each text message and
moves each message to a new list called sent_messages as it’s printed. After
calling the function, print both of your lists to make sure the messages were
moved correctly'''

short_messages = [
    'hello! I am Jarvis!',
    'I am optimus prime!',
    "Hi, we've been trying to reach you about your car's extended warranty'",
]

sent_messages = []


def show_messages(messages):
    for message in messages:
        print(f"{message.capitalize()}")

def send_messages(messages):
    while messages:
        current_message = messages.pop()
        print(f"{current_message.capitalize()}")
        sent_messages.append(current_message)
    

print(f"Short messages list: {short_messages}")
print(f"Sent messages list: {sent_messages}\n")

send_messages(short_messages)

print(f"\nShort messages list: {short_messages}")
print(f"Sent messages list: {sent_messages}")



# show_messages(short_messages)
