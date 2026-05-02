import pandas as pd

df = pd.read_json("Pandas/JsonData.json")

# filtering = Keeping the rows that match a condition

# Age = df[df["age"] >=30]
# print(Age)
# Department = df[df["department"] >= "IT" ]

# print(Department)
AgeDepartment = df[(df["age"] >= 30) | (df["department"] == "IT")]

print(AgeDepartment)

