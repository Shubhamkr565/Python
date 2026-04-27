import numpy as np


# Scalar Arithmetic (means: apply one number to all elements in array)

array = np.array([1, 2, 3])   # Create a NumPy array

print(array + 1)   
# Add 1 to each element → [2, 3, 4]

print(array - 2)   
# Subtract 2 from each element → [-1, 0, 1]

print(array * 3)   
# Multiply each element by 3 → [3, 6, 9]

print(array / 4)   
# Divide each element by 4 → [0.25, 0.5, 0.75]

print(array % 5)   
# Modulus (remainder after division by 5) → [1, 2, 3]

print(array ** 6)  
# Power operation (each element raised to power 6)
# → [1^6, 2^6, 3^6] = [1, 64, 729]











