Common Input/Output Mistakes
Mistake 1: Forgetting to convert input
# Wrong
age = input("Enter age: ")  # age is string "25"
next_age = age + 1  # ERROR!

# Correct
age = int(input("Enter age: "))
next_age = age + 1
Mistake 2: Converting non-numeric input to int
# If user types "hello" instead of a number:
age = int(input("Enter age: "))  # ERROR: invalid literal
✅ Fix: We'll learn error handling later. For now, make sure you enter correct data type.
Mistake 3: Concatenating string and number
# Wrong
age = 25
print("I am " + age)  # ERROR!

# Correct - Method 1
print("I am " + str(age))

# Correct - Method 2 (better)
print(f"I am {age}")

# Correct - Method 3
print("I am", age)  # print() handles it
Mistake 4: Forgetting space in prompt
# Not user-friendly
name = input("Enter name:")  # Enter name:Alice (no space!)

# User-friendly
name = input("Enter name: ") 