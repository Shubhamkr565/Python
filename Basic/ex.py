# python coding programs that cover basic to intermediate concepts

# Simple program to print "Hello World!"

# print("Hello World!")

# Program to add two numbers provides by the user

# print("Enter two number to add these number.\n")
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# sum = a+b
# print("Sum of Two number: ",sum)


# simple calcuator to perform basic operations 

# def calculate():
#     num1 = float(input("Enter first number: "))
#     num2 = float(input("Enter second number: "))

#     print("Choose Operation")
#     print("1. Add")
#     print("2. Sub")
#     print("3. Mul")
#     print("4. Div")

#     choice = int(input("Enter your choice (1,2,3,4): "))
#     if(choice == 1):
#         print(f"{num1}+{num2}= {num1+num2}")
#     elif(choice == 2):
#         print(f"{num1}-{num2}= {num1-num2}")
#     elif(choice == 3):
#         print(f"{num1}*{num2} = {num1*num2}")
#     elif(choice == 4):
#         print(f"{num1}/{num2} = {num1/num2}")
#     else:
#         print("Invalid Input")

# calculate()


# find the largest of three numbers

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# largest_number = 0

# if(a>=b and a>=c):
#     print("Largest number: ",a)
# elif(b>=a and b>=c):
#     print("Largest number: ",b)
# else:
#     print("largest number: ",c)



# factorial of a number
# def factorial(n):
#     if(n == 0 or n == 1):
#         return 1
#     else:
#         return n*factorial(n-1)

# num = int(input("Enter number to find the factorial: "))
# print(f"The factorial of {num} is {factorial(num)}") 


# check if a number is prime

# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num ** 0.5)+1):
#         if(num % i == 0):
#             return False
#     return True

# num = int(input("Enter a number to check prime or not: "))
# if(is_prime()):
#     print(f"{num} is a prime number.")


# Fibonacci Sequence

# def fibonacci(num):
#     a,b = 0,1
#     sequence = []
#     for i in range(num):
#         sequence.append(a)
#         a,b = b, a+b
#     return sequence
# num = int(input("Enter number of term: "))
# print(f"Fibonacci sequence up to {num} terms: {fibonacci(num)}")


# reverse a strig

# def reverse(str):
#     return str[::-1]

# str = str(input("Enter any String char: "))
# print(f"Reverse string: {reverse(str)}")

# palindrome

# def is_palindrome(str):
#     if(str == str[::-1]):
#         print("Yes this is palindrome")
#     else:
#         print("No this is not palindrome")
# str = str(input("Enter any char to check Palindrome: "))
# is_palindrome(str)



# bubble Sort

# def bubble(arr):
#     n = len(arr)

#     for i in range(n):
#         for j in range(0, n-i-1):
#             if(arr[j] > arr[j+1]):
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr

# arr= [54,232,556,767,74,2]
# print(f"Sorted array: {bubble(arr)}")

# linear search

# def linear_search(arr, num):
#     n = len(arr)
    
#     for i in range(n):
#         if(arr[i] == num):
#             return i
#     return -1

# arr = [10,30,49,5]
# num = 49

# result = linear_search(arr, num)
# if result!= -1:
#     print(f"Element found at index {result}")
# else:
#     print(f"Element not found")



# count the Occurences of a character in a string

# def count_char(str):
#     n = len(str)

#     for i in range(n):
#         count = 0

#         for j in range(n):
#             if(str[i] == str[j]):
#                 count += 1
#         print(str[i], "->", count)

# str = "abcda"
# count_char(str)

def merge_sorted(list1, list2):

    i = 0
    j = 0
    merged = []

    while i < len(list1) and j < len(list2):

        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1

    # remaining elements
    merged.extend(list1[i:])
    merged.extend(list2[j:])

    return merged


list1 = [1,2,7]
list2 = [3,4,6]

print(merge_sorted(list1, list2))