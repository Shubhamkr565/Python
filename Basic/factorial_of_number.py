print("Enter any number to find the factorial......")

def factorial(n):           #def is a keyword used to define a function. 
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)
num = int(input("Enter number: "))

print(f"The factorial of {num} is {factorial(num)}")