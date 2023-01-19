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
            x_direction = choice([-1, 1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            # y-axis; decide where to go
            y_direction = choice([-1, 1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_distance * y_direction

            # don't append move that are (0,0) ie. not going anywhere

            if x_step == 0 and y_step == 0:
                continue

            # calculate the new step
            x_new = self.x_values[-1] + x_step
            y_new = self.y_values[-1] + y_step

            self.x_values.append(x_new)
            self.y_values.append(y_new)
