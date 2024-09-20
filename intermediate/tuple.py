# Write a program to take a tuple of numbers from the keyboard and print its sum and
# average?

t = eval(input("Enter Tuple of number: "))
l = len(t)
sum = 0

for x in t:
    sum = sum+x
print("The sum is ",sum)
print("The average is ",sum/l)
