import pandas as pd

data = {"Name": ["Rohit", "Dhoni", "Virat", "Bumrah","Hardik"], 
        "Age": [38, 45, 37,35, 33]}

df = pd.DataFrame(data, index = ["Batsman1","Keeper", "Batsman2", "Bowler", "AllRounder"])

# print(df)

# print(df["Name"])

# print(df.loc["Bowler"])

# Add new column        

df["IPL Team"] = ["MI", "CSK","RCB","MI", "MI"]

# print(df)

# Add a new row

new_row = pd.DataFrame([{"Name": "Sanju","Age":32, "IPL Team": "CSK"},
                        {"Name": "Shreyas","Age":32, "IPL Team": "PK"}],
                       index=["Batsman+Keeper", "Batsman"])

df = pd.concat([df, new_row])
print(df)