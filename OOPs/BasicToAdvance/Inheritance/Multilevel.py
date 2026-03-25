class A:
    def showA(self):
        print("A")

class B(A):
    def showB(self):
        print("B")

class C(B):
    def showC(self):
        print("C")


X1 = C()

X1.showA()
X1.showB()
X1.showC()

Y1 = B()

try: 
    Y1.showA()
    Y1.showB()
    Y1.showC()
except AttributeError:
    print("Some method are not available in Class B")