# Variables: Variable are name given an value in python.
# unlike other programming languages we do not need to declare a type of the variable

# syntax variable_name = value 

a = 10
 
b = "String"

c = True

# memory management: 

# if 
# a = 10     Memory location: RC1
# b= 20     Memory location: RC2
# a = 30    Memory location: RC1
# keyword id we can use to get the location of the variable

a1 = 20
print(id(a1))

b1 = 30
print(id(b1))

a1 = 50
print(id(a1))