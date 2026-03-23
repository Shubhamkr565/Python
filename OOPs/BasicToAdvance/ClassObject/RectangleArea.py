# Find area of rectangle using class
# 🧠 Steps
# Store length & width
# Create method area()


class AreaOfRectange:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    

length = int(input("Enter Length of Rectangle: "))
width = int(input("Enter width of Rectangle: "))


r = AreaOfRectange(length, width)

print(f"Area of Rectangle: {r.area()}")