# It is a good practice to always close the file when you are done with it.

# If you are not using the with statement, you must write a close statement in order to close the file:

f = open("File Handling/file.txt")
print(f.readline())
print(f.readlines())

f.close()

# Note: You should always close your files. In some cases, due to buffering, changes made to a file may not show until you close the file.