Part 5: Indentation - Python's Superpower (and Weakness!)
Indentation defines code blocks in Python. This is UNIQUE to Python!
Correct:
if age >= 18:
    print("Adult")  # 4 spaces indentation
    print("Can vote")  # 4 spaces indentation
Wrong:
if age >= 18:
print("Adult")  # ERROR: IndentationError
Wrong:
if age >= 18:
    print("Adult")  # 4 spaces
      print("Can vote")  # 6 spaces - ERROR: inconsistent
Rule: Use 4 spaces consistently (or 1 tab, but never mix them!)