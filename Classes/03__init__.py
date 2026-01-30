"""All classes have a built-in method called __init__(), which is always executed when the class is being initiated.

The __init__() method is used to assign values to object properties, or to perform operations that are necessary when the object is being created."""

#  __init__() method is called automatically every time the class is being used to create a new object.

class Person:
    def __init__(self, name, age):
        self.personName = name
        self.personAge = age

    
p1 = Person("Kajal", 25)
# p2 = Person()

print(p1.name)
print(p1.age)
# print(p2.age)