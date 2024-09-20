s = "abcdabcdbabcd"

d = {}  # Empty dictionary to store character frequencies
for x in s:
    if x in d:
        d[x] = d[x] + 1  # If character exists, increment its count
    else:
        d[x] = 1  # If character doesn't exist, initialize its count to 1

# Loop through the dictionary and print the character frequencies
for k, v in d.items():
    print("{} = {} times".format(k, v))
