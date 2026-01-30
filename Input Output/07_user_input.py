Input from User with input()
Now let's make programs interactive!
Syntax:
variable = input(prompt_message)

Example 1: Basic input
name = input("What is your name? ")
print("Hello,", name)
When you run this:
What is your name? Alice
Hello, Alice


Important: input() Always Returns a String!
This is VERY important to understand:
# Taking age as input
age = input("Enter your age: ")
print(type(age))  # <class 'str'> ← It's a string!

# This will NOT work as expected:
next_age = age + 1  # ERROR! Can't add 1 to string
Why? Because input() always returns a string, even if you type a number!