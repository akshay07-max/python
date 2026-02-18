# 06_append_write_create.py

# To write to an existing file, you must add a parameter to the open() function:

# "a" - Append - will append to the end of the file.

# "w" - Write - will overwrite any existing content.


with open("File Handling/demotxt.txt", "a") as f:
    f.write("This is the text I'm writing in demotxt file usinf \'a\'(append), it will append to the existing content.")

with open("File Handling/demotxt.txt") as f:
    print(f.read())

