# 📝 Exercise 2 — Selection & Filtering Medium
# Using the student DataFrame from Exercise 1:
# Select only the "Name" and "Marks" columns
# Filter students who scored more than 70 marks
# Select the student at row index 2 using iloc
# Filter students with Age > 18 AND Marks > 75


import pandas as pd

data = pd.read_json("Pandas/Student_Exercises/CreateAndExplore/DataFrame.json")

print("\nOnly the Name: and Marks: Columns\n")
print(data[["Name", "Marks"]])

print("\nFilter Student who scored more than 70 marksn\n")
print(data[data["Marks"]>70])

print("\nAt row index 2\n")
print(data.iloc[2])

print("\nStudent with age > 18 and marks > 75\n")
print(data[(data["Age"]>18)& (data["Marks"]>75)])