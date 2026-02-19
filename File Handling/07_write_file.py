# write_file.py

filename = "sample1.txt"

with open(filename, "w") as file:
    data = input("Enter some text: ")
    file.write(data)

print("Data written successfully!")
