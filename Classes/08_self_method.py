class Person:
    def __init__(myObj, name):
        myObj.name = name

    def greet(myObj, age):
        return "Hello Buddy "+ myObj.name + " age is " + str(age)
    
    def getGreet(myObj):
        return myObj.greet(23)
    

p1 = Person("Akshay")

print(p1.getGreet())