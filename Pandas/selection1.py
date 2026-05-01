import pandas as pd

data = pd.read_json("Pandas/JsonData.json")

# print(data)

# using selection 

# print(data.to_string())

# print(data["id"])

# print(data[["id", "name"]])

# selection by rows

# print(data.loc[0])

print(data.iloc[11])