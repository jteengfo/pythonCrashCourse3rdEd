'''Make a list or tuple containing a series of 10 numbers and 5 letters.
Randomly select 4 numbers or letters from the list and print a message saying that
any ticket matching these 4 numbers or letters wins a prize.'''

import random

tuple = ('A', 'B', 'C', 'D', 'e', 1,2,3,4,5,6,7,8,9,99)
winners = []

while len(winners) < 4:
    chosen_winner = random.choice(tuple)

    if chosen_winner not in winners:
        winners.append(chosen_winner)
        print(f"Congratulations {chosen_winner}! You have won a prize!")