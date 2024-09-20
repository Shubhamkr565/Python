# Write a program to display unique vowels present in the given word?
vowel = {"a", "e", "i", "o", "u"}

word = input("Enter any word or sentence to find the vowels present in this sentence or word \n").lower()

found = set()


for letter in word:
    if letter in vowel:
        found.add(letter)
       

print("Unique vowels found:", found)
print("Total number of unique vowels present in this word/sentence is", len(found))
