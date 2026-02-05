class Car:
   def __init__(self, name, brand):
        self.name = name
        self.brand = brand
  
   def move(self):
      return f"drive"


class Airplane:
    def __init__(self, name, brand):
       self.name = name
       self.brand = brand

    def move(self):
        retunr f"Fly"