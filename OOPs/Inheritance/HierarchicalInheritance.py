# One Parent -> Multiple Children

class School:
    def School_name(self):
        print(f"School name AND Public School")


class Student(School):   # inheritance
    def Student_name(self):
        Name = str(input("Enter Your Name: "))
        print(f"Student name: {Name}")

class Teacher(School): # inheritance
    def Teacher_name(self):
        TName = str(input("Enter Teacher Name: "))
        print(f"Teacher Name: {TName}")


s1 = Student()
t1 = Teacher()

print("\n ---- Student Info -----")
s1.School_name()
s1.Student_name()

print("\n ---- Teacher Info -----")
t1.School_name()
t1.Teacher_name()