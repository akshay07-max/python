# copy_file.py

source = "sample1.txt"
destination = "sample2.txt"

with open(source, "r") as src:
    data = src.read()

with open(destination, "w") as dest:
    dest.write(data)

print("File copied successfully!")
