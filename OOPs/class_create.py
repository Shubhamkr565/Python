# class className:
    # """Documentation String"""
    # variable: instance variable, static variable, local variable
    # methods: instance methods, static methods, class methods


class Student:
    """This is Student class with required data"""
    def __init__(self):
        self.name = "Shubham"
        self.roll = 10
        self.marks = 95

    def introduction(self):
        print(self.name)
        print(self.roll)
        print(self.marks)

print(Student().introduction())
s1 = Student()
print(s1.introduction())

# print(Student().__doc__)
# help(Student)