class Employee:
    def __init__(self, name):
        self.name = name

class Manager(Employee):
    def show(self):
        print(self.name)

m1 = Manager("Shubham")

m1.show()