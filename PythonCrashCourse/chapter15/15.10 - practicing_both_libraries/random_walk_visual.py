from random_walk2 import RandomWalk
import plotly.express as px


# create random walk instance 
rw = RandomWalk()
rw.fill_walk()

# plot 
fig = px.scatter(rw.x_values, rw.y_values)
fig.show()
