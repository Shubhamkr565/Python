# Constructor overloading is not posible in Python
# If we define multiple constructors then the last constructor will be considered. 

class Demo:

    def __init__(self):
        print("NO arg constructor")
    
    def __init__(Self,a):
        print("One arg added constructor")

    def __init__(self,a,b):
        print("Two arg added constructor")


# d1 = Demo()

# d1 = Demo(10)

d1 = Demo(10,20)