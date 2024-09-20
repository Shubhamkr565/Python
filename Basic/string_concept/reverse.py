# Q1. Write a program to reverse the given String

# name = "Shubham"
# print(name[::-1])  #[::-1]: This is a slicing operation. The slicing syntax generally follows the pattern [start:stop:step], where:
# start: The index to start slicing from.
# stop: The index to stop slicing (not inclusive).
# step: The interval or step size between each element in the slice.

# 2nd method

# name = "Shubham"
# n = len(name)

# i = -1
# while i >= -n:
#     print(name[i], end='')
#     i = i-1

# 3rd method

name = "Shubham"

print("".join(reversed(name)))