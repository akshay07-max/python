class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        if(age>0):
            self.__age = age
        else:
            return "Invalid Age"


p1 = Person("Akshay", 23)

totalAge = p1.get_age()
print(totalAge)

p1.set_age(34)

print(p1.get_age())
