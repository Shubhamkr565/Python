import pandas as pd

# # Series = A pandas 1-Dimensional labeled array that can hold any data type. Think of it like a single column in a spreadsheet (1-Dimensional)

# data = [100, 102,104]
# data1 = [100.4, 103.34, 105.4534]
# data2 = ["A", "B", "C"]
# data3 = [True, False, True]

# series = pd.Series(data)
# print(series)

# series1 = pd.Series(data1)
# print(series1)

# series2 = pd.Series(data2)
# print(series2)

# series3 = pd.Series(data3)
# print(series3)





data = [100, 102, 104]

series = pd.Series(data, index=["emp 1:", "emp 2:", "emp 3:"])

# print(series)
# print(series.loc["emp 2:"])

series.loc["emp 2:"] = 200
# print(series.loc["emp 2:"])

print(series[series > 150])


