import matplotlib.pyplot as plt
import numpy as np

# Bar Chart = compare categories of data by representing each category with a bar

categories = np.array(["Grains", "Fruits", "Vegetables", "Protein", "Dairy", "Sweets"])
values = [4,3,2,5,3,1]

def labelStyle():
    return{
        "fontsize":20,
        "family":"Arial",
        "fontweight":"bold",
        }

plt.title("Daily consumption", fontdict=labelStyle())
plt.xlabel("Food",  fontdict=labelStyle())
plt.ylabel("Quantity",  fontdict=labelStyle())




plt.bar(categories, values, color="Green")
plt.show()