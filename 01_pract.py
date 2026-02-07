class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"Name: {self.name}, Salary: {self.salary}")


class Developer(Employee):   # Inheriting Employee
    def __init__(self, name, salary, language):
        super().__init__(name, salary)  # call parent constructor
        self.language = language

    def show_details(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Language: {self.language}")


dev = Developer("Akshay", 60000, "Python")
dev.show_details()