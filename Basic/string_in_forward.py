# Q. Write a program to access each character of string in forward and backward direction
# by using while loop?


s = "My name is Shubham Kumar"
n = len(s)
i = 0

print("Forward direction")
while i<n:
    print(s[i], end='')
    i = i+1

print("backward direction")
i = -1
while i >= -n:
    print(s[i], end='')
    i = i-1
