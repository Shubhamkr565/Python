import pandas as pd

calorise = {"Day1": 1750, "Day2": 2100, "Day3": 1700}

series = pd.Series(calorise)

series.loc["Day3"] +=400
print(series[series<2000])