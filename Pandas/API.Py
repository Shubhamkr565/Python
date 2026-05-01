import pandas as pd

data = pd.read_json("Pandas/JsonData.json")

# print(data.to_string())

# print(data.head())
# print(data.columns)

# print(data[data["city"]=="Mumbai"])


# print(data["salary"].mean())

# print(data.groupby("department")["salary"].mean())

print(data.loc[data["salary"].idxmax()])  # loc is used when row accesses iloc also