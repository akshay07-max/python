class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def fullName(self):
        return f"My full name is {self.fname} {self.lname}"


p1 = Person("Akshay", "Surase")

print(p1.fullName())