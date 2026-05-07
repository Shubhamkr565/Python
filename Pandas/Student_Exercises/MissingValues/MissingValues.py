"""Create a DataFrame containing:

Name
Age
City
Salary

Add some missing values (NaN) manually.

Then:
Print the first 3 rows using head()
Print the shape of the DataFrame
Print all column names

Select only the "Name" and "Age" columns
Filter emp who Salary more than 7000 
Select the emp at row index 2 using iloc
Filter emp with Age > 18 AND Salary > 75000

Count missing values in each column
Fill missing Age with average age
Fill missing City with "Unknown"
Drop rows containing missing Salary
Save cleaned data into CSV"""

import pandas as pd

data = pd.read_csv("Pandas/Student_Exercises/MissingValues/DataFrame.csv")

# print(data.to_string())

print("\n===== First 3 row using head ========\n")
print(data.head(3))

print("\n ===== Shape of the DataFrame =======\n")
print(data.shape)


print("\n ====== All Column Name =======\n")
print(data.columns)

print("\n ===== Name and Age ======\n")
print(data[["Name", "Age"]])

print("\n ====== Salary more than 7000 ======\n")
print(data[data["Salary"]> 70000])

print("\n======= emp at row index 2 =======\n")
print(data.iloc[2])

print("\n====== Filter emp with Age > 18 AND Salary > 75000 ======== \n")
print(data[(data["Age"]>18) & (data["Salary"]>75000)])

print("\n======== Count missing values in each column  ========\n")
print(data.isnull().sum())


print("\n======== Fill missing Age with average age =========\n")
avg = int(data["Age"].mean())
data["Age"] = data["Age"].fillna(avg)

print(data)


print("\n======= Fill missing City with ""Unknown"" ========\n")
data["City"] = data["City"].fillna("Unknown")
print(data)

print("\n======= Drop rows containing missing Salary =======\n")
data = data.dropna(subset=["Salary"])
print(data) 


print("\n======== Save cleaned data into CSV ========\n")
data.to_csv("Clean_data.csv", index = False)

print("Clean data saved successfully")