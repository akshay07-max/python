# Properties  the variables that belongs to the class. they store data  for each object created from the class.

# accessing object property with dot
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

car1 = Car("Toyota", "Corolla")

print(car1.brand)
print(car1.model)