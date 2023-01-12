'''
Make a class Die with one attribute called sides, which has a
default value of 6. Write a method called roll_die() that prints a random number between 1 and the number of sides the die has. Make a 6-sided die and
roll it 10 times.
Make a 10-sided die and a 20-sided die. Roll each die 10 times.'''

import random

class Die:
    ''' A class representing a dice object.'''
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_die(self):
        '''A method that rolls the die.'''
        rolled_number = random.randint(1,self.sides)
        print(f"You rolled a {rolled_number}!")

# six sides
six_sided_die = Die()
for turn in range(6):
    six_sided_die.roll_die()

# 10 sides
ten_sided_die = Die(10)
for turn in range(10):
    ten_sided_die.roll_die()

# 20 sides
twenty_sided_die = Die(20)
for turn in range(20):
    twenty_sided_die.roll_die()
