class Student:
    """This is Student class with required data """
    def __init__(self,name,roll,marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def introduction(self):
        print("Name of the student: ",self.name)
        print("Roll no of the student: ",self.roll)
        print("Marks of the student: ",self.marks)

s1 = Student("Shubham",2,90)
s1.introduction()
