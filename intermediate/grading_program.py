#  you have access to a database of student_scores in the format of a dictionary.
# the keys in student_score are the names of the student and the values are there exam scores.

student_score = {
    "Shubham" : 81,
    "Amit" : 78,
    "Ron" : 81,
}


student_grade = {}

for student in student_score:
    score = student_score[student]
    if score > 90:
        student_grade[student] = "Outstanding"
    elif score > 80:
        student_grade[student] = "Exceeds Expectation"
    elif score > 70:
        student_grade[student] = "Acceptable"
    elif score < 70:
        student_grade[student] = "fail"

print(student_grade)