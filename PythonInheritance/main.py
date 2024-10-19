# inheritance = allows a class to inherit attributes and methods from another class
#               helps with code reusability and extensibility
#               class Child(Parent)
#               sub(Super)
from warnings import catch_warnings


class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True
    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is asleep")

class Dog(Animal):
        def speak(self):
            print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

class Mouse(Animal):
    def speak(self):
        print("Squeak!")

dog = Dog("Sasha")
cat = Cat("Bob")
mouse = Mouse("Jerry")

print(mouse.name)
print(mouse.is_alive)
mouse.eat()
#mouse.sleep()
mouse.speak()