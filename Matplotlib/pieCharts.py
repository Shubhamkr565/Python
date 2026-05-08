import matplotlib.pyplot as plt
import numpy as np

# Bar chart = Circular chart divided into slices to show percentages of the totla.
#               Good for visualizing distribution amongs categories.

categories = ["Freshmen", "Sophomores", "Juniors", "Seniors"]
values =np.array([300, 250, 275, 225])
colors = ["red", "yellow", "blue", "green"]
plt.pie(values, labels=categories, 
                autopct= "%1.1f%%",
                colors=colors,
                explode=[0,0,0,0.2],
                shadow=True,
                startangle=180)

plt.title("Bro code College")
plt.show()