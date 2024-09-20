# You are going to write a program that calculates the average student height from a List of heights.

student_height = input("Enter Student height:\n ").split()

for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])

print(student_height)    

total_height = 0

for height in student_height:
    total_height += height
print(total_height)

total_student = 0

for student in student_height:
    total_student += 1
print(total_student)

average_height = total_height / total_student

print(average_height)

# eg [156, 178, 165, 171, 187]