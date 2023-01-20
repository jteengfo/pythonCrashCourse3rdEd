from die import Die
import plotly.express as px

# create two D8s
die_1 = Die(8)
die_2 = Die(8)

# do 1000 rolls 
results = []
for roll in range(1_000_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# analyze the results 
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
die_sides = range(2, max_result+1)

for side in die_sides:
    frequency = results.count(side)
    frequencies.append(frequency)

# visualize the results 
title = "Results of Rolling two D8s"
labels = {
    'x' : 'Die Sides',
    'y' : 'Frequencies',
}

fig = px.bar(x=die_sides, y=frequencies, title=title, labels=labels)
fig.show()
