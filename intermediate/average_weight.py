student_weight = input("Enter student weight: \n").split()

for w in range(0, len(student_weight)):
    student_weight[w] = int(student_weight[w])

print(student_weight)

total_student = 0

for no_of_student in student_weight:
    total_student += 1
print(total_student)

total_weight = 0
for weights in student_weight:
    total_weight += weights
print(total_weight)

average_weight = total_weight / total_student

print(average_weight)