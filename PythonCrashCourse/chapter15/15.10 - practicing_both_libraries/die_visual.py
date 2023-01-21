
import matplotlib.pyplot as plt 
import plotly.express as px
from die import Die


# create die
die_1 = Die()

# roll die n times 
results = [die_1.roll() for roll in range(1_000_000)]

# analyze data 
poss_results = range(1, die_1.num_sides+1)
frequencies = [results.count(poss_result) for poss_result in poss_results]

# visualize data -- matplotlib
plt.style.use('classic')
plt.bar(poss_results, frequencies)
plt.show()


# visualize data -- pyplot 
# fig = px.bar(x=poss_results, y=frequencies)
# fig.show()