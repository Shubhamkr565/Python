class Parent:
    def __init__(self):
        pass

    def fun1(self):
        print("Inside fun1() of parent class")
    
    def fun2(self):
        print("Inside fun2() of parent classs")

class child(Parent):
    def fun2(self):
        print("Inside fun2() of child class")
        super().fun2()

c1 = child()
print(c1)

c1.fun1()
c1.fun2()   
c1.fun2()

print("is subclass (child, parent)")
