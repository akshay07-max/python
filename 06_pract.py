class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")


# Object creation
s1 = Student("Akshay", 22)
s2 = Student("Rahul", 21)

s1.display()
s2.display()