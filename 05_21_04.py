class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def show(self):
        print(self.name)

class Developer(Employee):   # Inheritance
    def show(self):          # Polymorphism
        print("Developer:", self.name)

e1 = Developer("Akshay", 50000)
e1.show()