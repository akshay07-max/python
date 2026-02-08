class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        return self.salary


class Manager(Employee):
    def get_salary(self):
        return self.salary + 5000


e = Employee("Amit", 30000)
m = Manager("Neha", 30000)

print(e.get_salary())   # 30000
print(m.get_salary())   # 35000