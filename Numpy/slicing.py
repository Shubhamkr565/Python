import numpy as np;
import time

start = time.time()
array = np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])


# print(start:end:step)
# print(array[::])

print(array[0:3])

end = time.time()
print("Execution time: ", end-start," seconds")