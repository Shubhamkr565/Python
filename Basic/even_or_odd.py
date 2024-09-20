def check(n):
    if n % 2 == 0:
        print(f"{n} is a Even Number: ")
    else:
        print(f"{n} is a Odd Number:")

num = int(input("Enter number to check even or odd: "))

check(num)

