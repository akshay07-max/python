# Read Only Parts of the File
# By default the read() method returns the whole text, but you can also specify how many characters you want to return:
with open("File Handling/file.txt") as f:
    print(f.read(5))

    