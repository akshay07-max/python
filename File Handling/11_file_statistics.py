# file_statistics.py

filename = "sample1.txt"

with open(filename, "r") as file:
    content = file.read()

lines = content.split("\n")
words = content.split()
characters = len(content)

print("Lines:", len(lines))
print("Words:", len(words))
print("Characters:", characters)
