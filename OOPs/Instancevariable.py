# class Car:
#     def __init__(self, make, model, year):
#         # These are instance variables
#         self.make = make
#         self.model = model
#         self.year = year

#     def car_info(self):
#         return f"{self.year} {self.make} {self.model}"

# # Creating instances of the Car class
# car1 = Car("Toyota", "Camry", 2020)
# car2 = Car("Honda", "Civic", 2019)

# # Accessing instance variables
# print(car1.car_info())  # Output: 2020 Toyota Camry
# print(car2.car_info())  # Output: 2019 Honda Civic




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
