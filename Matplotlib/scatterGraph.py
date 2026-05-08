import matplotlib.pyplot as plt
import numpy as np

# scatter graph = Shows the relationship between two variables Helps to identify a correlation
#   (+,-,None) Example: Study hours vs. Test scores


x1 = np.array([0,1,1,2,3,4,5,6,7,7,8]) # Hours Studied
y1 = np.array([55,60,65,62,68,70,75,78,82,85,87])# grades

x2 = np.array([0,1,1,2,3,4,5,6,7,7,8]) # Hours Studied
y2 = np.array([50,58,65,72,78,83,88,89,92,95,97])# grades


plt.scatter(x1,y1, color="skyblue",
                    label="class A")

plt.scatter(x2,y2, color="green",
                    label="Class B")



plt.title("Test Scores")
plt.xlabel("Hours Studied")
plt.ylabel("Grade")

plt.legend()

plt.show()