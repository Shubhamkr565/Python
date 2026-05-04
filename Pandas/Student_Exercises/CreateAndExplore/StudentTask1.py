# 📝 Exercise 1 — Create & Explore Beginner
# Create a DataFrame of 5 students with columns: Name, Age, Marks (out of 100).
# Print the first 3 rows using head()
# Print the shape of the DataFrame
# Print all column names
# Get basic statistics using describe()



import pandas as pd

data = pd.read_json("Pandas/Student_Exercises/CreateAndExplore/DataFrame.json")

print("Full Data\n")
print(data)

print("\nFirst 3 rows using head()\n")
print(data.head(3))

print("\nShape of the DataFrame: \n")
print(data.shape)


print("Columns Name: \n")
print(data.columns)


print("\nBasic Statistics:\n")
print(data.describe())