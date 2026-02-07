class Vehicle:
    def __init__(self, speed):
        self.__speed = speed  # encapsulation

    def get_speed(self):
        return self.__speed

    def move(self):
        print("Vehicle is moving")


class Car(Vehicle):
    def move(self):  # polymorphism
        print("Car is moving at", self.get_speed(), "km/h")


class Bike(Vehicle):
    def move(self):  # polymorphism
        print("Bike is moving at", self.get_speed(), "km/h")


vehicles = [Car(120), Bike(80)]

for v in vehicles:
    v.move()