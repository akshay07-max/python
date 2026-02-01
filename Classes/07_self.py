class BioData:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return(f"Hello, Good Morning. My name is {self.name}, and I'm {self.age} years old");

    def grt(self):
        return(f"Hello good morning..")

p1 = BioData("Akshay", 23)
print(p1.greet())
print(p1.grt())
