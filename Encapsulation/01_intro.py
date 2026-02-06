# The encapsulation in python is keeping the main class data safe while accessing from the outside
# It is about the protecting the data inside a class.
# It means keeping data (properties) and methods together in a class, while controlling how the data can be accessed from outside the class.
# This prevents accidental changes to your data and hides the internal details of how your class works.

# private properties in python: you can make properties by just usinf __propName

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age


p1 = Person("Akshay", 23)

print(p1.name)
print(p1.__age)  # cause an error

# Note: Private properties cannot be accessed directly from outside the class.