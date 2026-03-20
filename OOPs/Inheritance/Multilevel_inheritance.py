# Grandparent -> parent -> Child


# Base Class
class Vehicle:
    def start(self):
        print("Vehicle is Starting.....")

# Child Class (Level 1)
class Car(Vehicle):
    def fuel_tupe(self):
        print("Car uses fuel or petrol/diesel")

# Child class (Level 2)

class ElectricCar(Car):
    def battery_status(self):
        print("Battery is Fully Charged.")

# Create Object of Electric Car
car1 = ElectricCar()

car1.start()
car1.fuel_tupe()
car1.battery_status()

