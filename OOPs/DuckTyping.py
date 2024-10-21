class Dog:
    def talk(self):
        print("Bow  Bow")

class Cat:
    def talk(self):
        print("Meow Meow")

class Duck:
    def talk(self):
        print("Quack   Quack")


def fun1(obj):
    obj.talk()

# i = [Duck(), Cat(), Dog()]
# for obj in i:
#     fun1(obj)

d = Duck()
fun1(d)

d = Dog()
fun1(d)

d = Cat()
fun1(d)