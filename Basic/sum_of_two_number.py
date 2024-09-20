
# a = 10
# b = 20

# print("Sum of two number = ",a+b)


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

sum = a+b

print(f"The sum of {a} and {b} = {sum}") # The f before the string in the print function is used to denote an f-string in Python. F-strings, introduced in Python 3.6, allow you to embed expressions inside string literals, using curly braces {}.

# or

print("The sum of {} and {} = {}".format(a, b, sum))


