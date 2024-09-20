def check(n):
    if n >= 1 and n <=100:
        print(f"Yes {n} is the range between 1 to 100! ")
    else:
        print(f"No {n} is not the range between 1 to 100! ")

num = int(input("Enter number: "))
check(num)