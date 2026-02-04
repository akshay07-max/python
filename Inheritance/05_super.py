# Python also has a super() function that will make the child class inherit all the methods and properties from its parent:

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def fullName(self):
        return f"{self.fname} {self.lname}"
    

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        # self.graduationyear = 2019
        self.graduationyear = year


# s1 = Student("Akshay", "Surase")

s1 = Student("Akshay", "Surase", 2023)

print(s1.fullName())
# print(s2.fullName())

# In the example below, the year 2019 should be a variable, and passed into the Student class when creating student objects. To do so, add another parameter in the __init__() function:
print(s1.graduationyear)

# By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.