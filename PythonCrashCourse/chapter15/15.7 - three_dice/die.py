from random import randint

class Die:
    ''' A class representing a die '''
    def __init__(self, num_sides=6):
        ''' Initialize attributes of a die object '''
        self.num_sides = num_sides

    def roll(self):
        ''' Rolls the die and returns an int between 1 to num_sides '''
        result = randint(1, self.num_sides)
        return result 