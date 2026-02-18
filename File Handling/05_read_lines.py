with open("File Handling/file.txt") as f:
    print(f.readline())
    print(f.readline()) # reads next line not the same one (2rd line)
    print(f.readline()) # reads next line not the same one (3rd line)


# using loops

with open("File Handling/file.txt") as f:
    for x in f:
        print(x)


