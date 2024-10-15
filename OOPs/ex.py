# class Employee:
#     """Inside the constructor by using self variabel"""
#     def __init__(self):
#         self.empId = 10
#         self.empName = "Shubham"
#         self.salary = 120000

# emp1 = Employee()
# print(emp1.__dict__)




# class Demo:
#     """Inside the instance method by using self variable"""
#     def __init__(self):
#         self.a = 10
#         self.b = 20

#     def fun1(self):
#         print("inside fun1 method of demo class")
#         self.c = 30

# d1 = Demo()
# print(d1.__dict__)

# d1.fun1()
# print(d1.__dict__)



# class Demo:
#     """Outside the class using object variable"""

#     def __init__(self):
#         self.a = 10
#         self.b = 20

#     def fun1(self):
#         print("inside fun1 method of Demo class")
#         self.c = 30

# d1 = Demo()

# print(d1.__dict__)
# d1.fun1()
# print(d1.__dict__)
# d1.d = 40
# print(d1.__dict__)




# Accessing an instance variable:

# class Demo:
#     def __init__(self):
#         self.a = 100
#         self.b = 200

#     def fun1(self):
#         print("Inside fun1 method of Demo class")
#         print("a value is ",self.a)
#         print("b value is ",self.b)

# d1 = Demo()
# d1.fun1()
# print("Outside of class")
# print("a value is ",d1.a)
# print("b value is ",d1.b)





# Delete instance variable from the object

# class Demo:
#     def __init__(self):
#         self.a = 100
#         self.b = 200
#         self.c = 300
#         self.d = 400
        
#     def fun1(self):
#         print("inside fun1 method from Demo class") 
#         print("deleting the variable d")
#         del self.d

# d1 = Demo()
# print(d1.__dict__)
# d1.fun1()
# print(d1.__dict__)
# del d1.c
# print(d1.__dict__)

# d2 = Demo()
# print(d2.__dict__)

# print("Change the value of d1.a = 500")
# d1.a = 500
# print(d1.__dict__)
# print(d2.__dict__)




class Demo:
    def __init__(self):
        self.a = 100
        self.b = 200
        self.c = 300
        self.d = 400

    def fun1(self):
        print("Inside the fun1 method from Demo class")

d1 = Demo()

d2 = d1

d1.a = 500
d1.b = 1000

d2.c = 150
d2.d = 450

print(d1.__dict__)

print(d2.__dict__)



