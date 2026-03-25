# ✅ 1. Same Method Name, Different Behavior

# 👉 Ask:

# "Is the method name same but working differently?"

# ✔ Example:

# class Dog:
#     def sound(self):
#         print("Bark")

# class Cat:
#     def sound(self):
#         print("Meow")

# 👉 Same method sound() → different output ✅



# ✅ 2. Method Overriding (Inheritance Case)

# 👉 Ask:

# "Is child class changing parent method?"

# ✔ Example:

# class Animal:
#     def sound(self):
#         print("Animal sound")

# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")

# 👉 Same method overridden → polymorphism ✅




# ✅ 3. Same Function, Different Object

# 👉 Ask:

# "Am I calling same method on different objects?"

# ✔ Example:

# animals = [Dog(), Cat()]

# for a in animals:
#     a.sound()

# 👉 Same call → different output ✅



# ✅ 4. Operator Polymorphism (Important)

# 👉 Ask:

# "Same operator doing different work?"

# ✔ Example:

# print(5 + 3)        # 8
# print("Hi " + "Bro")  # Hi Bro

# 👉 + → addition + string join ✅