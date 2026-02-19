filename = "sample1.txt"

with open(filename, "a") as file:
    data = input("Enter text to append: ")
    file.write("\n" + data)

print("Data appended successfully!")
