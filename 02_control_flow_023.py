Part 3: The if Statement - Basic Syntax
Syntax:
if condition:
    # code block to execute if condition is True
    statement1
    statement2
Key points:
if keyword
Condition (must evaluate to True or False)
Colon :
Indentation (4 spaces or 1 tab) - VERY IMPORTANT!
Part 4: Your First if Statement
age = 18

if age >= 18:
    print("You are an adult")
    print("You can vote")
Output:
You are an adult
You can vote
What happened:
Python checks: Is age >= 18? → Is 18 >= 18? → True
Since True, Python executes the indented block
Both print statements run
Try with different value:
age = 15

if age >= 18:
    print("You are an adult")
    print("You can vote")

print("This always runs")
Output:
This always runs
Why?
Condition 15 >= 18 is False
Indented block is skipped
"This always runs" is not indented, so it always executes