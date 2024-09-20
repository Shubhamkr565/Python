# Write a program to enter name and percentage marks in a dictionary and
# display information on the screen


student_detail = {}
n = int(input("Enter number of student: "))

i = 1

while i<=n:
    s_name = input("Enter Student name: ")
    s_roll = int(input("Enter student roll_no: "))
    s_marks = int(input("Enter student marks: "))
    i = i+1

print("Name of student:","\t"," % of marks")

for name, marks in student_detail.items():
    print("\t",name ,"\t",marks)

