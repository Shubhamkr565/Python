import numpy as np
# import time

# start = time.time()
# Vectorized math func
# array = np.array([1,2,3])
# array2 = np.array([1.343, 5.232, 454.34])
# print(np.sqrt(array))

# print(np.round(array2))

# print(np.floor(array2))

# print(np.pi * array ** 2)



# Element wise arithmetic 

# array1 = np.array([1,2,3])
# array2 = np.array([4,5,6])

# print(array1+array2)

# print(array1-array2)

# print(array1*array2)

# print(array1/array2)



# Comparison Operators

marks = np.array([89,65,100,45,67,91])

print(marks == 100)

print(marks >= 60)

marks[marks < 60] = 0

print(marks)







# end = time.time()

# print("Execution time: ", end-start," seconds")