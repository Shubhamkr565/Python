#  Program to merge characters of 2 strings into a single string by taking characters
# alternatively.

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

i , j= 0 , 0
result = ""

while i<len(first_name) or j<len(last_name):
    if i<len(first_name):
        result = result + first_name[i]
        i += 1
    if j<len(last_name):
        result = result + last_name[j]
        j += 1

print(result)