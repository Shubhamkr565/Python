class Person:

    def __init__(self, name, age):
        self.name=name
        self.age=age

    def personalDetails(self):
        print("Personal Details: Name is {0} and age is {1}".format(self.name, self.age))



class Employee(Person):

    def __init__(self, name, age, email, sal):
        super().__init__(name, age)
        self.email=email
        self.sal=sal

    def professionalDetails(self):
        print("Professional Details: Email is {0} and salary is {1}".format(self.email, self.sal))


e1 = Employee("Ram",25,"ram@gmail.com",80000)

e1.personalDetails()
e1.professionalDetails()
