# Q2. Program to reverse order of words.

def reverse_words(sentence):
    # Split the sentence into words
    words = sentence.split()
    
    # Reverse the list of words
    reversed_words = words[::-1]
    
    # Join the reversed words back into a string
    reversed_sentence = ' '.join(reversed_words)
    
    return reversed_sentence

# Test the function
sentence = "Program to reverse order of words"
print(reverse_words(sentence))
