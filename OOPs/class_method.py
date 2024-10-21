class Animal:
    legs = 4
    @classmethod
    def walk(cls,name):
        print("{} walks in {} legs".format(name,cls.legs))

Animal.walk("cat")
Animal.walk("Dog")


# Program to track number of objects created for a class

class Demo:
    count = 0
    def __init__(self):
        Demo.count = Demo.count+1

    @classmethod
    def getNumberOfObjectCreated(cls):
        print("The number of object created for the demo class is: ",cls.count)
    
d1 = Demo()
d2 = Demo()
d3 = Demo()

Demo.getNumberOfObjectCreated()