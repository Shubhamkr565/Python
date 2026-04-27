import numpy as np

# broadcasting allow Numpy to perform operation on arrays
# with different shapes by virtually expanding dimensions
# so they match the larger arrays shape

# The dimension have the same size.
# or
# One of the dimension has a size 1.

# NumPy can do operations on arrays of different shapes by automatically expanding them.

# array1 = np.array([[1,2,3,4]])
# array2 = np.array([[1],[2],[3],[4]])

# print(array1.shape)
# print(array2.shape)

# print(array1 * array2)


# Write Table from 1 to 10 using broadcasting 

arr1 = np.array([[1,2,3,4,5,6,7,8,9,10]])
arr2 = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])


print(arr1*arr2)

