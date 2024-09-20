# Write a program to remove duplicate characters from the given input string?

s = "aabbccdd"  # Input string
result = ""     # To store the final result without duplicates
duplicate = []  # List to track already encountered characters

# Loop through each character in the input string
for x in s:
    # If the character is not already in 'duplicate', add it to the result
    if x not in duplicate:
        duplicate.append(x)  # Track the character in 'duplicate' list
        result += x          # Add the character to the result string

# Print the final result with duplicates removed
print(result)
