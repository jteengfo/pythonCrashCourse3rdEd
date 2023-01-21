'''When you roll two dice, you usually add the two numbers
together to get the result. Create a visualization that shows what happens if you
multiply these numbers by each other instead.'''

import plotly.express as px
from die import Die


# create two dice
die_1 = Die()
die_2 = Die()

# roll them to get results 
results = []
for roll in range(5_000_000):
    result = die_1.roll() * die_2.roll()
    results.append(result)

# analyze the data 
frequencies = []
mult_result = range(1, die_1.num_sides*die_2.num_sides + 1)
for mult in mult_result:
    frequency = results.count(mult)
    frequencies.append(frequency)

# visualize analysis
title = "Results of Rolling two D6s and Multiplying their Numbers"
labels = {
    'x' : 'Numbers',
    'y' : 'Frequencies'
}

fig = px.bar(x=mult_result, y=frequencies, title=title, labels=labels)
fig.show()
