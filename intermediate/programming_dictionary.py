programming_dicitionary = {
    "introduction": "Python is a high-level, interpreted, and general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python emphasizes code readability with its simple syntax.\n",

    "Key Features": "Easy to Read and Write, Interpreted Language, Dynamically Typed, Extensive Libraries, ect.\n",

    "Data Types": "Basic: int, float, bool, str. Collections: list, tuple, set, dict \n",
    "Control Flow": "Conditional Statements: if, elif, else. Loops: for, while. Functions: Defined using def keyword.\n",

    "OOP": "Classes and Objects, Inheritance, Polymorphism, Encapsulation \n",

    "Applications": "Web Development (Django, Flask), Data Science and Machine Learning (pandas, NumPy, scikit-learn), Scripting and Automation, Game Development (Pygame), GUI Applications (Tkinter, PyQt)\n",

    "Popularity": "Python is widely used due to its simplicity and versatility, making it a popular choice in fields like AI, ML, web development, and automation."
}

# Retrieving items from dicitionary. 
print(programming_dicitionary["OOP"])

# Adding new items to dicitionary.
programming_dicitionary["Loop"] = "The action of doing something over and over again."

# Create an empty dicitionary.
empty_dicitionary = {}

# Edit an item in a dicitionary.
programming_dicitionary["introduction"] = "Python is a high-level, interpreted programming language known for its simplicity and readability."

# Loop through a dictionary

for key in programming_dicitionary:
    print(key)