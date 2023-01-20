import matplotlib.pyplot as plt


squares = [1, 4, 9, 16, 25,]
input = [1, 2, 3, 4, 5]


x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

fig, ax = plt.subplots()
# ax.plot(input, squares, linewidth = 3)
# ax.scatter(input, squares, s=50)

ax.plot(x_values, y_values, linewidth = 2)
ax.scatter(x_values, y_values, s=5)
plt.show()