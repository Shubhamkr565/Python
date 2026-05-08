import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023,2024,2025,2026])
y1 = np.array([15,26,3,32])
y2 = np.array([45,56,34,72])
y3 = np.array([57,6,38,12])
y4 = np.array([45,16,83,12])

def labelStyle():
    return{
        "fontsize":20,
        "family":"Arial",
        "fontweight":"bold",
        }
plt.title("Class Size", fontdict=labelStyle(),
                        color="orange")

plt.xlabel("Year",fontdict=labelStyle(),
                    color="green")

plt.ylabel("Students", fontdict= labelStyle(),
                    color="blue")

plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)
plt.plot(x,y4)

plt.show()