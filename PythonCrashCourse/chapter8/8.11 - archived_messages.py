'''
: Start with your work from Exercise 8-10. Call the function send_messages() with a copy of the list of messages. 
After calling the function, print both of your lists to show that the original list has retained its messages'''

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

send_messages(short_messages[:])

print(f"\nShort messages list: {short_messages}")
print(f"Sent messages list: {sent_messages}")

