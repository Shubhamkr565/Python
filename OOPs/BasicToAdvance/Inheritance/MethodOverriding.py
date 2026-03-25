class Animal:
    def speak(self):
        print("Animal Make Sound....")

class Dog(Animal):
    def speak(self):
        print("Dog Sound Bark Bark...") #Method overriding


d1 = Dog()

d1.speak()

A1 = Animal()

A1.speak()