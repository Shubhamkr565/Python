class Student:
    def __init__(self, name, roll, marks): #constructor
        self.name = name    # using Encapsulation
        self.roll = roll
        self.marks = marks

    def show_details(self):     # Method
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll}")
        print(f"Marks: {self.marks}")

    def update_marks(self):   # Method
        new_marks = int(input("Enter new marks: "))
        self.marks = new_marks
        print(f"Marks update successfully!")

s1 = Student("Shubham", 1,90)
s2 = Student("Rahul", 2,45)


print("\n --- Student 1 Details ---")
s1.show_details()

print("\n --- updating Student 1 Details ---")
s1.update_marks()

print("\n --- Updating Details ---")
s1.show_details()

