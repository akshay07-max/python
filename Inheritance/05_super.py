# Python also has a super() function that will make the child class inherit all the methods and properties from its parent:

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def fullName(self):
        return f"{self.fname} {self.lname}"
    

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)


s1 = Student("Akshay", "Surase")

print(s1.fullName())