# Class methods are the functions that belongs to a class and define the behavior of the objects created from the class.

class Person:
    def __init__(self, name, age):
        self.name = name

    def greet(self):
        return f"Hello my name is {self.name}"
    

p1 = Person("Akshay", 24)
print(p1.greet())