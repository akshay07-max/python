filename = "sample1.txt"

with open(filename, "r") as file:
    content = file.read()

print("File Content:")
print(content)
