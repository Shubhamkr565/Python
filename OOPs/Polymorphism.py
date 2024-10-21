class Demo:

    def sum(self, a=None, b=None, c=None):
        if a!=None and b!=None and c!=None:
            print("sum of 3 numbers are:",(a+b+c))
        elif a!=None and b!=None:
            print("sum of 2 numbers are:",(a+b))
        else:
            print("please provide 2 or 3 arguments")


d1 = Demo()

d1.sum(10,20,30)
d1.sum(10,20)
d1.sum(10)