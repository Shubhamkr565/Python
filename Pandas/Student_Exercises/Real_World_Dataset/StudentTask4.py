#  Exercise 4 — Real World Dataset Advanced
# Load the Titanic CSV (or any CSV you have). Then:
# Show how many passengers survived vs. didn't using value_counts()
# Find average age of survivors vs. non-survivors using groupby()
# Find the 5 oldest passengers using sort_values()
# Count how many missing values exist in each column
# Save the cleaned DataFrame to a new CSV file

import pandas as pd

data = pd.read_csv("pandas/Student_Exercises/Real_World_Dataset/TitanicData.csv")

# print(data.to_string())


print("\n======= passengers survived ========= \n")
print(data["Survived"].value_counts())


print("\n====== average age of survivors ========\n")
print(data.groupby("Survived")["Age"].mean())

print("\n====== 5 Oldest Passengers ========")
print(data.sort_values(by="Age", ascending=False).head(5))

print("\n=======Missing Values =======")
print(data.isnull().sum())


data.to_csv("cleaned_titanic.csv", index=False)

print("\n✅ Cleaned CSV file saved successfully!")



















"""
```python id="l3dfp4"
# ============================================================
# 📝 Exercise 4 — Real World Dataset Advanced
# ============================================================

# Import pandas library
# Pandas is used for data analysis and working with CSV files
import pandas as pd


# ============================================================
# Load Titanic CSV file into a DataFrame
# ============================================================

# read_csv() reads the CSV file
# and stores the data inside variable "data"
data = pd.read_csv("pandas/Student_Exercises/Real_World_Dataset/TitanicData.csv")


# ============================================================
# Display full dataset (Optional)
# ============================================================

# to_string() prints complete DataFrame without cutting rows
# Uncomment this line if you want to see all data

# print(data.to_string())


# ============================================================
# Count survived vs non-survived passengers
# ============================================================

print("\n======= passengers survived ========= \n")

# data["Survived"]
# Accesses the "Survived" column

# value_counts()
# Counts how many times each value appears

# In Titanic dataset:
# 1 = Survived
# 0 = Did not survive

print(data["Survived"].value_counts())


# ============================================================
# Find average age of survivors and non-survivors
# ============================================================

print("\n====== average age of survivors ========\n")

# groupby("Survived")
# Groups data based on Survived column

# ["Age"]
# Select only Age column

# mean()
# Calculates average age of each group

print(data.groupby("Survived")["Age"].mean())


# ============================================================
# Find 5 oldest passengers
# ============================================================

print("\n====== 5 Oldest Passengers ========")

# sort_values(by="Age", ascending=False)
# Sorts Age column from highest to lowest

# head(5)
# Shows first 5 rows after sorting

print(data.sort_values(by="Age", ascending=False).head(5))


# ============================================================
# Count missing values in each column
# ============================================================

print("\n=======Missing Values =======")

# isnull()
# Detects missing values (NaN)

# sum()
# Counts total missing values in each column

print(data.isnull().sum())


# ============================================================
# Save DataFrame into new CSV file
# ============================================================

# to_csv()
# Saves DataFrame into a CSV file

# index=False
# Prevents pandas from saving row index numbers

data.to_csv("cleaned_titanic.csv", index=False)


# ============================================================
# Success Message
# ============================================================

print("\n✅ Cleaned CSV file saved successfully!")
```


"""