Type Casting (Converting Data Types)
To use input as numbers, we must convert (cast) them!
Type Casting Functions:
int() - Convert to integer
float() - Convert to float
str() - Convert to string
bool() - Convert to boolean


Converting to Integer
# Method 1: Convert after input
age_str = input("Enter your age: ")
age = int(age_str)
print(type(age))  # <class 'int'>

# Method 2: Convert during input (better!)
age = int(input("Enter your age: "))
print(type(age))  # <class 'int'>

# Now you can do math
next_age = age + 1
print(f"Next year you'll be {next_age}")
Example run:
Enter your age: 25
<class 'int'>
Next year you'll be 26


Converting to Float
height = float(input("Enter your height in feet: "))
print(f"Your height is {height} feet")
print(type(height))  # <class 'float'>
Example run:
Enter your height in feet: 5.8
Your height is 5.8 feet
<class 'float'>

Converting to String
# Number to string
age = 25
age_str = str(age)
message = "I am " + age_str + " years old"
print(message)  # I am 25 years old

# Or use f-string (easier!)
message = f"I am {age} years old"
print(message)