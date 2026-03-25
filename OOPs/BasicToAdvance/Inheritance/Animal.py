class Animal:
    def speak(self):
        print("Animal speak")

class Dog(Animal):
    def bark(self):
        print("Dog Barks")

d = Dog()
d.speak()
d.bark()




# ✅ Basic Syntax
# class Parent:
#     # properties & methods

# class Child(Parent):
#     # inherits Parent


# ✅ 5 Tips to Identify Inheritance in a Program

# 1. Check Parent Class

# "Is there a base class?"
# class Animal:

# 2. Check Child Class Syntax

# class Dog(Animal):

# 👉 (Animal) → inheritance happening ✅


# 3. Check Reuse of Code
# "Is child using parent method?"

# d.eat()

# 👉 No need to rewrite → inheritance

# 4. Check Additional Features

# 👉 Child can add new methods:

# def bark(self):

# 👉 Parent + Child features together

# 5. Check Object Behavior
# "Object of child can use both methods?"

# d = Dog()

# d.eat()   # parent
# d.bark()  # child

# 👉 YES → Inheritance confirmed ✅

# ⚡ Types of Inheritance (Quick View)

# Single Inheritance
# class B(A)

# Multilevel
# class C(B)

# Multiple
# class C(A, B)

# Hierarchical
# class B(A)
# class C(A)

# 🎯 Final Shortcut

# 👉 Inheritance =
# Parent class + Child class + Code reuse