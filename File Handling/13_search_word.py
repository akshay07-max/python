# search_word.py

filename = "sample1.txt"
search_word = input("Enter word to search: ")

found = False

with open(filename, "r") as file:
    for line_number, line in enumerate(file, start=1):
        if search_word in line:
            print(f"Word found at line {line_number}")
            found = True

if not found:
    print("Word not found.")
