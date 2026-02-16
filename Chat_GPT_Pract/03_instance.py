class Employee:
    company = "Google"  # Class variable

    def __init__(self, name):
        self.name = name  # Instance variable

e1 = Employee("Akshay")
e2 = Employee("Rahul")

print(e1.company)  # Google
