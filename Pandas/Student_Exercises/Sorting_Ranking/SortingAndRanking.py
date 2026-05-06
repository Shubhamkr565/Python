"""Create a DataFrame of employees with columns:

Name
Department
Salary
Experience

Then:

Show the top 3 highest salaries using sort_values()
Find the employee with lowest salary
Sort employees by Experience in descending order
Display only Name and Salary columns
Find average salary of all employees
"""

import pandas as pd

data = pd.read_json("Pandas/Student_Exercises/Sorting_Ranking/DataFrame.json")

# print(data.to_string())

print("\n====== top 3 highest salaries =========")
HS = data.sort_values(by="Salary", ascending=False).head(3)
print(HS)


print("\n====== top 3 lowest salaries =========")

LS = data.sort_values(by="Salary", ascending=True).head(3)
print(LS)

print("\n====== Employee with lowest salaries ========")

LS1 = data.sort_values(by="Salary", ascending=True).head(1)

print(LS1)


print("\n======== Employees by Experience in descending order ======= ")

EE = data.sort_values(by="Experience", ascending=False)

print(EE)

print("\n========= Display only Name and Salary columns ========= ")

print(data[["Name", "Salary"]])


print("\n ======== average salary of all employees =======")
AS = data["Salary"].mean()

print(AS)

