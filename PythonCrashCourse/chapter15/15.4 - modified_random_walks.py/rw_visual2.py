import matplotlib.pyplot as plt 
from random_walk2 import RandomWalk


while True:
    # create randomwalk instance
    rw = RandomWalk()
    rw.fill_walk()

    # plot 
    plt.style.use('classic')
    fig, ax = plt.subplots()
    ax.scatter(rw.x_values, rw.y_values, s=15)
    # ax.plot(rw.x_values, rw.y_values, linewidth=3)
    ax.set_aspect('equal')
    plt.show()


    keep_running = input("Do you want to make another random walk? (y/n): ")
    if keep_running == 'n':
        break


