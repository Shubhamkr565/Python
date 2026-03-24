import math
class AreaOfCircle:
    def __init__ (self, r):
        self.r = r

    def area(self):
        return math.pi*self.r**2

radius = float(input("Enter radius of Circle : "))
C1 = AreaOfCircle(radius)

print(f"Area of Circle: {C1.area():.2f}")