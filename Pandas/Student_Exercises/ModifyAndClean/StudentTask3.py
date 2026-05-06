# 📝 Exercise 3 — Modify & Clean Medium
# Continuing from Exercise 1:
# Add a new column "Grade": A if Marks≥90, B if ≥75, else C
# Add a column "Passed" that is True if Marks ≥ 50
# Set one Marks value to NaN, then fill it with the column mean
# Drop the "Age" column from the DataFrame



import pandas as pd


data = pd.read_json("Pandas/Student_Exercises/CreateAndExplore/DataFrame.json")

print(data.to_string())

def give_grade(Marks):
    if Marks >=90:
        return "A"
    elif Marks >=75 and Marks <90:
        return "B"
    else:
        return "C" 

def passed(Marks):
    if Marks >= 50:
        return True

data["Grade"] = data["Marks"].apply(give_grade)
data["Passed"] = data['Marks'].apply(passed)


data = data.drop("Age", axis=1)
print(data.to_string())




