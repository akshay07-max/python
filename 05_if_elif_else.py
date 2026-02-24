Part 9: Multiple Conditions with if-elif-else
What if you have more than two options?
Syntax:
if condition1:
    # code if condition1 is True
elif condition2:
    # code if condition1 is False and condition2 is True
elif condition3:
    # code if previous conditions False and condition3 is True
else:
    # code if all conditions are False
Example: Grade Calculator
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is: {grade}")
Output:
Your grade is: B
How it works:
Check 85 >= 90? → False, skip
Check 85 >= 80? → True, execute grade = "B", stop checking
Skip all remaining elif/else blocks
Print result
Important: Only ONE block executes! Once a condition is True, Python stops checking.