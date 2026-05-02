import pandas as pd

data = pd.read_json("Pandas/JsonData.json")


# print(data.mean(numeric_only=True))
# print(data.sum(numeric_only=True))

# print(data.min(numeric_only=True))

# print(data.max(numeric_only=True))

# print(data.count(numeric_only=True))



print(data["salary"].mean())
print(data.sum(numeric_only=True))

# print(data.min(numeric_only=True))

# print(data.max(numeric_only=True))

# print(data.count(numeric_only=True))