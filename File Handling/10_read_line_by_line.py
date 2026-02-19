# read_line_by_line.py

filename = "sample1.txt"

with open(filename, "r") as file:
    for line in file:
        print(line.strip())
