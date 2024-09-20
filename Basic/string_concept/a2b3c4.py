# write a program for the following requirement



s = "a2b3c4"  # Input string containing letters followed by digits
result = ""   # Empty string to store the final output

# Loop through each character in the input string 's'
for x in s:
    
    # Check if the character is a letter
    if x.isalpha():
        result = result + x  # Add the letter to the result string
        number = x           # Store the letter in 'number' for future use in the else block
    
    # If the character is not a letter (it is a digit)
    else:
        # Convert the digit to an integer, subtract 1, and repeat the previous letter that many times
        result = result + number * (int(x) - 1)

# Print the final result string
print(result)
