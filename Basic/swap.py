a = 50
b = 100


# XOR swap
# a = a ^ b  # Step 1: a becomes a ^ b
# b = a ^ b  # Step 2: b becomes (a ^ b) ^ b, which is a
# a = a ^ b  # Step 3: a becomes (a ^ b) ^ a, which is b

# a = a+b
# b = a-b
# a = a-b

c = a
a = b
b = c

print(a)
print(b)