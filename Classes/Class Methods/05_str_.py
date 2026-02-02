# The __str__() method is a special method that controls what is returned when the object is printed:

# Without the __str__() method:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)
print(p1)

