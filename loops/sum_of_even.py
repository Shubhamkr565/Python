# Write a program to find the sum of even number between 1 to 100 including 1 or 100 


sum  = 0

for number in range(2, 101, 2):
    # print(number)
    sum += number
print(sum)


total = 0
for number in range(1 , 101):
    if number % 2 == 0:
        total += number
print(total)