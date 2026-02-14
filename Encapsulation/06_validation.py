class Student:
    def __init__(self, name, grade):
        self.name = name
        self.__grade = grade

    def get_grade(self):
        return self.__grade

    def set_grade(self, grade):
        self.__grade = grade


s1 = Student("Akshay", 89)
print(s1.name)
# print(s1.__grade) # Error
print(s1.get_grade())  # grade = 89

s1.set_grade(90)

print(s1.get_grade()) # grade = 90


