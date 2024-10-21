class Calculator:

    @staticmethod
    def add(x,y):
        print(f"Sum of two number is {x+y}")

    @staticmethod
    def sub(x,y):
        print(f"Sub of two number is {x-y}")

    @staticmethod
    def mul(x,y):
        print(f"Mul of two number is {x*y}")

c1 = Calculator()

c1.add(5,7)
c1.sub(10,4)
c1.mul(5,2)