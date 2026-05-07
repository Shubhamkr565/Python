"""Create a sales DataFrame with columns:

Product
Category
Sales
Quantity

Then:

Find total sales of each category using groupby()
Find average quantity sold for each product
Find highest sales product
Count how many products belong to each category
Sort products by Sales"""

import pandas as pd

data = pd.read_json("Pandas/Student_Exercises/GroupBy/DataFrame.json")

# print(data.to_string())

print("\n====== total sales of each category =======")

TSEC = data.groupby("Category")["Sales"].sum()

print(TSEC)

print("\n====== average quantity sold =======")

# AQS = data.groupby("Quantity")["Sales"].mean()
AQS = data.groupby("Product")["Quantity"].mean()

# print(AQS)
print(AQS)


print("\n===== Total products belong to each category =======")

TP = data.groupby("Product")["Category"].sum()
TP2 = data[["Product", "Category"]]

print(TP)
print(TP2)


print("\n===== products by Sales ======")

PBS = data.sort_values(by="Sales", ascending=False)


print(PBS)