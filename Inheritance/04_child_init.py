# So far we have created a child class that inherits the properties and methods from its parent.
# We want to add the __init__() function to the child class (instead of the pass keyword).
# Note: The __init__() function is called automatically every time the class is being used to create a new object.

class Person:
    def __init__(self, fname, lname):
        self.name = fname
        self.lname = lname

    def fullName(self):
        return f"Name is {self.fname} {self.lname}"
    

