import pandas as pd

data = pd.read_json("Pandas/JsonData.json")


# print(data)
# Drop irrelevant columns
df = data.drop(columns=["salary"])

# handle missing data
df = df.dropna(subset=["name"])

print(df.to_string())