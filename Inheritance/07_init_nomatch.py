# To Test: what if the arguments of init of child class not matches with the arguments of the parent class in init?
# Result not it throws an error, the same properties should be present in the init of child class. Name can be different but the matching props should be there.

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
    
    def welcome(self):
        print("Welcome", self.fname, self.lname, "to the class of", self.graduationyear)

# s1 = Student()