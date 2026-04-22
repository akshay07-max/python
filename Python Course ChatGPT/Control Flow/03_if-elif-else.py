# Used when multiple conditions

marks = 36

if marks >= 85:
    print(f"congratulations... you got Grade 'A'")

elif marks >= 75 and marks < 85:
    print("Grade 'B'")

elif marks >= 50 and marks < 75:
    print("Grade 'B'")


else:
    print("Kya gunda banega re tuuuu....")

# marks >= 90 ? No
# marks >= 75 ? Yes
# Print B Grade


# Important Rule

# Python checks top to bottom.

# Once one condition becomes True → rest skipped.

x = 95

if x > 50:
    print("Pass")
elif x > 90:
    print("Excellent")

# Pass will be he output


