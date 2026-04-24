# Used to combine conditions.   

# | Operator | Meaning      |
# | -------- | ------------ |
# | and      | Both true    |
# | or       | Any one true |
# | not      | Reverse      |

age = 25
salary = 50000

if age > 18 and salary > 30000:
    print("Eligible")
# Both must be true.

# or Example

day = "Sunday"

if day == "Sunday" or day == "Saturday":
    print("Holiday")
