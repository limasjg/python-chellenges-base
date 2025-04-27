# Object Orientation (POO) is a programming paradigm where we create classes to serve as a model and from there create objects, 
# each with its own attributes and methods.

class celphone:

    num_cel = 0

    def __init__(self,brand, memory ):
        self.brand = brand
        self.memory = memory
        celphone.num_cel += 1
    
    def show_phone(self):
        print(f"My fone is a {self.brand} and your memory is {self.memory}")

phone1 = celphone("Samsung", "512gb")
phone2 = celphone("Iphone", "128gb")
phone3 = celphone("Motorola", "256gb")



phone1.show_phone()
phone2.show_phone()
phone3.show_phone()

print(f"I have {celphone.num_cel} phones")