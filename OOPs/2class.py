# Defining a static method inside the class which accepts the object of another class:

class Student:
    def __init__(self,name,roll,marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def display(self):
        print(f"Nama = {self.name}")
        print(f"Roll = {self.roll}")
        print(f"Marks = {self.marks}")

class Demo:
    @staticmethod
    def modify(obj):
        obj.marks = obj.marks + 50
        obj.display()

s1 = Student("Ram",1,100)

s1.display()

Demo.modify(s1)
s1.display()