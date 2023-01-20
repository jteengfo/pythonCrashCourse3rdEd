from die import Die
import plotly.express as px

# Create 3 D6 dice
die_1 = Die()
die_2 = Die()
die_3 = Die()

# Roll 3 D6 dice n times 
results = []
for roll in range(5_000_000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

# Analyze results 
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
die_sides = range(3,max_result)
for side in die_sides:
    frequency = results.count(side)
    frequencies.append(frequency)

# Visualize results 
title = "Results of Rolling two D6s"
labels = {
    'x' : 'Results',
    'y' : 'Frequencies'
}
fig = px.bar(x=die_sides, y=frequencies, title=title, labels=labels)
fig.show()