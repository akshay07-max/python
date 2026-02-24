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