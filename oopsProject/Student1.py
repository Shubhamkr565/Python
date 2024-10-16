# Create Student class that takes name and marks of 3 subjects as arguments in constructor.
# then create a method to print the average

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi ", self.name, "Your avg score is: ", sum/3)

s1 = Student("Shubham",[98, 96, 97])
s1.get_avg()

s2 = Student("Amit",[93, 76,87])
s2.get_avg()

s3 = Student("Rohit",[90, 69, 88])
s3.get_avg()
