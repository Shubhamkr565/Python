# Create Student class that takes name and marks of 3 subjects as arguments in constructor.
# then create a method to print the average


class Student:
    def __init__(self, name, math,phy,chem):
        self.name = name
        self.math = int(math)
        self.phy = int(phy)
        self.chem = int(chem)

    def method1(self):
        print("Name of the Student: ",self.name)
        print("Marks obtain in Math: ",self.math)
        print("Marks obtain in Phy: ",self.phy)
        print("Marks obtain in Chem: ",self.chem)

    def average(self):
        sum = self.math+self.phy+self.chem
        average = sum/3
        return average 

s1 = Student("Shubham",80,75,80)
s1.method1()
print(s1.average())
s2 = Student("Aman",70,85,70)
s2.method1()
print(s2.average())
s3 = Student("Rohit",90,65,60)
s3.method1()
print(s3.average())
