# there are three ways to format a string
#1. f- string

name = "Akshay"
age = 24
gender = "Male"

message = f"Hello, My name is {name}, i am {age} years old {gender})

print(message)

a= 100
b = 20
print(f"sum: {a+b})

# formatting numbers
pi =3.1415
print(f"PI rounder: {pi: .2f})

price = 1234.5
print(f"Price: ${price:.2f}")
# Output: Price: $1234.50

# Thousands separator
population = 1000000
print(f"Population: {population:,}")
# Output: Population: 1,000,000

# 2. format (old but working)
name1 = "Akshay"
age1 = 24

message= "My name is {}, and I'm {} years old".format(name, age)

print(message)

# With index numbers
message = "My name is {0}, I am {1} years old. Yes, {0}!".format(name, age)
print(message)
# Output: My name is Bob, I am 30 years old. Yes, Bob!

# With names
message = "My name is {n}, I am {a} years old".format(n=name, a=age)
print(message)
# Output: My name is Bob, I am 30 years old