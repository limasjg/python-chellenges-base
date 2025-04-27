class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True
    
    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Dog(Animal):
    def speak(self):
        print("WOOF")

class Cat(Animal):
    def speak(self):
        print("MEOW")

class Mouse(Animal):
    def speak(self):
        print("SQUEEk")

animal1 = Dog("Krypto")
animal2 = Cat("Luke")
animal3 = Mouse("Mikey")

animal2.speak()
animal3.speak()
animal1.speak()

