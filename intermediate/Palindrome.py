def is_Palindrome(s):
    return s == s[::-1]

s = input("Enter any string to check it is Palindrome or not: ")

if is_Palindrome(s):
    print(f"{s} is a Palindrome....")
else:
    print(f"{s} is not a Palindrome...")
