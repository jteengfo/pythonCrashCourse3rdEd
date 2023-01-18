''''
A number raised to the third power is a cube. Plot the first five
cubic numbers, and then plot the first 5,000 cubic numbers.'''

import matplotlib.pyplot as plt

# x & y values
x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

# selecting a style
plt.style.use('seaborn-v0_8-pastel')
fig, ax = plt.subplots()
ax.plot(x_values, y_values)
ax.scatter(x_values, y_values)

# set axes titles and graph title
ax.set_title('Cubic Numbers', fontsize=25)
ax.set_xlabel('X Value', fontsize=14)
ax.set_ylabel('X^3 Value', fontsize=14)
plt.show()
