# you are going to write a program to that calculate the height score from the list of score.

student_score = input("Enter student score: \n").split()

for n in range(0, len(student_score)):
    student_score[n] = int(student_score[n])
print(student_score)

height_score = 0

for score in student_score:
    if score  > height_score:
        height_score = score
print(height_score)


# print(max(student_score))