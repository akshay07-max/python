Part 6: Comparison Operators
To create conditions, we use comparison operators:
Operator
Meaning
Example
Result
==
Equal to
5 == 5
True
!=
Not equal to
5 != 3
True
>
Greater than
5 > 3
True
<
Less than
5 < 3
False
>=
Greater than or equal
5 >= 5
True
<=
Less than or equal
3 <= 5
True
Examples:
# Equal to
x = 10
if x == 10:
    print("x is 10")  # This runs

# Not equal to
if x != 5:
    print("x is not 5")  # This runs

# Greater than
age = 25
if age > 18:
    print("Adult")  # This runs

# Less than
temperature = 15
if temperature < 20:
    print("It's cold")  # This runs

# Greater than or equal
score = 60
if score >= 60:
    print("Passed")  # This runs

# Less than or equal
if score <= 100:
    print("Valid score")  # This runs



Part 7: Comparing Different Data Types
Strings:
name = "Alice"

if name == "Alice":
    print("Hello Alice!")  # This runs

# String comparison is case-sensitive!
if name == "alice":
    print("This won't run")  # Different case
Booleans:
is_raining = True

if is_raining:  # No need for == True
    print("Take umbrella")

# Same as:
if is_raining == True:
    print("Take umbrella")
Mixed types (be careful!):
# Comparing int and float works
if 5 == 5.0:
    print("Equal")  # This runs

# Comparing number and string doesn't work as expected
x = 5
if x == "5":
    print("Equal")  # This WON'T run (different types)