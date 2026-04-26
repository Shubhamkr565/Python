import numpy as np;
import time

start = time.time()
array = np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])


# print(start:end:step)
# print(array[::])

# print(array[::-2])

# print(array[0:2, 1:])

print(array[0:2, 0:2])

end = time.time()
print("Execution time: ", end-start," seconds")