class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show(self):
        print("Brand:", self.brand)
        print("Model:", self.model)

# Object creation
c1 = Car("Toyota", "Fortuner")
c1.show()