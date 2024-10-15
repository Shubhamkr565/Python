# class Demo:
#     x = 10  # Static (class) variable, shared by all instances

#     def __init__(self):
#         self.y = 20  # Instance variable

# d1 = Demo()
# d1.y = 200  # Modify instance variable 'y'

# Demo.x = 100  # Modifying the static variable at the class level affects all instances

# print("d1", d1.y, d1.x)  # Access instance and class variables

# d2 = Demo()
# print("d2", d2.y, d2.x)  # Access instance and class variables

# print(d1.__dict__)  # Show instance variables of 'd1'
# print(Demo.__dict__)  # Show class variables and methods





# Various places to declare the static variables:

class Demo:
    x = 10  # Static variable, shared by all instances

    def __init__(self):
        Demo.b = 20  # Static variable initialized in constructor

    def fun1(self):
        Demo.c = 30  # Static variable assigned inside a method

    @classmethod
    def fun2(cls):
        Demo.d1 = 40  # Static variable using class reference
        cls.d2 = 50   # Static variable using cls reference

    @staticmethod
    def fun3():
        Demo.e = 60  # Static variable inside a static method

print(Demo.__dict__)  # Check class attributes

d1 = Demo()
print(Demo.__dict__)  # After creating an instance

d1.fun1()
print(Demo.__dict__)  # After calling instance method

Demo.fun2()
print(Demo.__dict__)  # After calling class method

Demo.fun3()
print(Demo.__dict__)  # After calling static method

Demo.f = 70  # Directly assigning a new static variable
print(Demo.__dict__)  # Final check of class attributes

