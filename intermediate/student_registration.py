# Write a program to student registration form using dictionary

student_registration = []

def new_student(name, email, contact):
    student = {}
    student["name"] = name
    student["emall"] = email
    student["contact"] = contact
    student_registration.append(student)

new_student("Shubham","Shubhamkr565@gmail.com", 9304788132)
print(student_registration)