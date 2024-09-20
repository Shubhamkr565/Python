# Write a program to sort the characters of the string and first alphabet symbols
# followed by numeric values

s = input("Enter mix alphabet and number: ")

s1 = s2 = result = ""

for x in s:
    if x.isalpha():
        s1 = s1+x
    else:
        s2 = s2+x

for x in sorted(s1):
    result = result + x
for x in sorted(s2):
    result = result + x
print(result)