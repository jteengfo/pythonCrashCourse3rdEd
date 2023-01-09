'''
 Write a program that polls users about their dream vacation. Write a prompt similar to If you could visit one place in the world, where
would you go? Include a block of code that prints the results of the poll.

'''

responses = {}

# setting a flag, indicating poll is active.
polling_active = True
repeat_active = True

# polling
while polling_active:
    name = input("What is your name?: ")
    response = input("If you could visit one place in the world, where would you go?: ")

    # storing polls into the dict
    responses[name] = response

    repeat = ''
    while repeat_active:
        repeat = input("Would you like to let another person response? yes/no?: ")
        if repeat == 'no':
            polling_active = False
            break
        elif repeat == 'yes':
            repeat_active = False
    # reset flag       
    repeat_active = True 

# polling complete, printing results 
print('\n --- Poll Results ---')
for name, response in responses.items():
    print(f"{name.capitalize()} would like to go to {response.title()}")