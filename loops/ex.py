marks = input("Enter student marks! \n").split()

for n in range(0, len(marks)):
    marks[n] = int(marks[n])

print(marks)

height_marks = 0

for heigh in marks:
    if height_marks < heigh:
        height_marks = heigh
print(height_marks)