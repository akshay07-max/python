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