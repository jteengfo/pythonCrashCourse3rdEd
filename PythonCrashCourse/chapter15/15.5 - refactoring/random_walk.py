
''' The fill_walk() method is lengthy. Create a new method
called get_step() to determine the direction and distance for each step, and then
calculate the step. You should end up with two calls to get_step() in fill_walk():

x_step = self.get_step()
y_step = self.get_step()


This refactoring should reduce the size of fill_walk() and make the
method easier to read and understand.
'''

from random import choice

class RandomWalk:
    '''A blueprint to creating a randomwalk obj.'''

    def __init__(self, num_points=5000):
        ''' Initalize attributes of random walk obj.'''
        self.num_points = num_points

        # start point at (0,0)
        self.x_values = [0]
        self.y_values = [0]
    
    def fill_walk(self):
        '''Generate walk points in a random walk.'''

        # keep generating walk points until num_points reached
        while len(self.x_values) < self.num_points:

            # x-axis; decide where to go
            x_step = self.get_step()
            y_step = self.get_step()
            # don't append move that are (0,0) ie. not going anywhere

            if x_step == 0 and y_step == 0:
                continue

            # calculate the new step
            x_new = self.x_values[-1] + x_step
            y_new = self.y_values[-1] + y_step

            self.x_values.append(x_new)
            self.y_values.append(y_new)
    
    def get_step(self):
        '''Calculates a step direction and distance.'''

        direction = choice([-1,1])
        distance = choice([0, 1, 2, 3, 5, 8, 13, 21])

        return direction * distance