class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        if self.name == "dog":
            return (f"The {self.name} Barks")
        
        elif self.name== "cat":
            return (f"The {self.name} says meo")
        
        else:
            return (f"{self.name} animal is not present in DB")
        

class getAnimal(Animal):
    pass


animal = getAnimal("dog")
print(animal.sound())
  