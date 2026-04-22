# Used when you want code to run only if condition is true.

# Syntax:
    # if condition:
    #     code

# Condition True? ---> Yes ---> Run Block
#                ---> No ----> Skip

age = 24

if age >= 18:
    print("You can drive now.")

k = 221

if k%2 == 0:
    print(f"The number {k} is even")

print("Exited")