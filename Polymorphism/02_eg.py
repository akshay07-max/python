# so the polymorphism in python is used when we have multiple classes having the same method.

# for eg we have classes Car, Airplane, Boat which has the same method move():

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        return f"you can drive {self.model}"
    

class Airplane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        return "Fly!"
    
class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        return "Sail!"
    

c1 = Car("Tata", "Fortuner")
a1 = Airplane("Boing", "Boing-717")
b1 = Boat("Cruise", "Volvo")

for x in (c1, a1, b1):
    print(x.move())
