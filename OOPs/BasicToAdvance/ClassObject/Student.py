# Define a class named Student
class Student:
    # Constructor method (called automatically when object is created)
    def __init__ (self,name,age):
        self.name = name
        self.age = age

     # Method to display student details
    def display(self):
        print(f"{self.name}, Age: {self.age}")


# Create an object of Student class
s1= Student("Shubham",20)

# Call the display method to show student details
s1.display()