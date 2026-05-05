import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023,2024,2025,2026])
y1 = np.array([15,25,30,20])
y2 = np.array([17,23,40,10])
y3 = np.array([10,6,22,36])


line_style = dict(marker=".", 
            markersize=10,
            markerfacecolor="green",
            markeredgecolor="yellow",
            linestyle="solid",
            linewidth=2,
            
            )

plt.plot(x,y1,color="pink", **line_style),
plt.plot(x,y2,color="blue", **line_style),
plt.plot(x,y3,color="green",  **line_style)
plt.show()
