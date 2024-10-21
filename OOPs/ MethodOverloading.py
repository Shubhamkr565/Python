# # fun1(int a)

# # fun1(double a)

# # But in Python Method overloading is not possible. 

# class Demo:
#     def fun1(self):
#         print("No arg method")
    
#     def fun1(self,a):
#         print("One arg added")

#     def fun1(self,a,b):
#         print("Two arg added")
    
# d1 = Demo()
# d1.fun1()
# d1.fun1(10)
# d1.fun1(10,20)

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