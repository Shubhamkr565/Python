class Student:
    def __init__(self):
        pass

    def setName(self,name):
        self.name = name
    
    def setRoll(self,roll):
        self.roll = roll
    
    def setMarks(self,marks):
        self.marks = marks

    def getName(self):
        return self.name
    
    def getRoll(self):
        return self.roll
    
    def getMarks(self):
        return self.marks
    
Students = []


while True:
    s1 = Student()

    name = input("Enter your Name:")
    roll = int(input("Enter Your Roll_no:"))
    marks = int(input("Enter Your Marks:"))

    s1.setName(name)
    s1.setRoll(roll)
    s1.setMarks(marks)

    Students.append(s1)

    choice = input("Want More: (y/n) ?")
    if choice == "n" or choice == "N":
        break

for student in Students:
    print("Name is: ",student.getName())
    print("Roll is: ",student.getRoll())
    print("Marks is: ",student.getMarks())
    print("============")