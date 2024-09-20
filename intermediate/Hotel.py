import random

cards = "Put all of your cards in this bowl: "

name_string = input("Enter the names of all friends present in this hotel (separated by commas): ")

names = name_string.split(", ")

total_friends = len(names)

waiter_prompt = "Please pick up only one card from this bowl: "

# Randomly select an index of one friend
waiter_index = random.randint(0, total_friends - 1)

# Print the selected friend's name
print(f"{waiter_prompt} The selected friend is: {names[waiter_index]}")
