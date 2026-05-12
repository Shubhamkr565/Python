# Task 1 — Your First Plot 
# Plot y = x² for x from -10 to 10. Add title, x/y labels, and grid. Make the line red.


import matplotlib.pyplot as plt
import numpy as np

# creating x value from -10 to 10

x = np.arange(-10, 11)

# calculate y = x^2

y = x**2

# plot the graph
plt.plot(x,y,color="red")


# title and labels
plt.title("Graph of y = x^2")
plt.xlabel("X Values")
plt.ylabel("Y values")

# show graph  
