# Used when have two choices

# syntax
    # if condition:
    #     code1
    # else:
    #     code2

#         Condition
#         /      \
#      True      False
#       |          |
#    code1       code2

num = 10

if num % 2 == 0:
    print(f"{num} is even")

else:
    print(f"{num} is odd")

print("Exited")

