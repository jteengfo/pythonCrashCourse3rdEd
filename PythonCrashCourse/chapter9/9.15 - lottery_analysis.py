'''. Lottery Analysis: You can use a loop to see how hard it might be to win
the kind of lottery you just modeled. Make a list or tuple called my_ticket. Write
a loop that keeps pulling numbers until your ticket wins. Print a message reporting how many times the loop had to run to give you a winning ticket.'''

from random import choice 
tuple = ('A', 'B', 'C', 'D', 'e', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

def get_random_ticket():
    ''' creates a random ticket to be compared with the winning ticket.'''
    ticket = []
    while len(ticket) < 4:
        chosen_element = choice(tuple)
        if chosen_element not in ticket:
            ticket.append(chosen_element)
    return ticket

def get_winning_ticket():
    ''' create the winning ticket.'''

    winning_ticket = []
    while len(winning_ticket) < 4:
        chosen_element = choice(tuple)
        if chosen_element not in winning_ticket:
            winning_ticket.append(chosen_element)
    return winning_ticket

def compare_tickets(my_ticket, winning_ticket):
    for element in my_ticket:
        if element not in winning_ticket:
            return False

    return True 

# create a winning ticket 
winning_ticket = get_winning_ticket()


# counter
count = 0
win = False

while not win:
    my_ticket = get_random_ticket()
    win = compare_tickets(my_ticket, winning_ticket)
    count += 1

if win:
    print("Congratulations! You have won!")
    print(f"Your ticket is {my_ticket}")
    print(f"The winning ticket is {winning_ticket}")
    print(f"It took {count} number of tries to win!")



    