# So far we have created a child class that inherits the properties and methods from its parent.
# We want to add the __init__() function to the child class (instead of the pass keyword).
# Note: The __init__() function is called automatically every time the class is being used to create a new object.

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def fullName(self):
        return f"Name is {self.fname} {self.lname}"
    

# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function
# Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.

# class Student(Person):
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname

#     def stdName(self):
#         return f"{self.fname} {self.lname}"
    
# std1 = Student("Akshay", "Surase")

# print(std1.stdName())

# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
        self.fname = fname
        self.lname = lname

    

S1 = Student("Akshay", "Surase")

print(S1.fullName())


# As you can see in the code we need to redeclare the person's properties duw to the init of the child class
# let's know about the super in python to overcome this.