num = [10,34,56,76,99,24,65]

i = 0
 
while i < len(num):
    if num[i] % 2 == 0:
        print(num[i]," is Even")
        i = i+1
    else:
        print(num[i], " is Odd")
        i = i+1