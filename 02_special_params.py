# separator:
# syntax sep(separator)
# by default pyhton has the space as a separator.

print("Apple", "Banana", "Papaya") #default

#custom sep
print("Apple", "Banana", "Papaya", sep="' ")

#custom sep
print("Apple", "Banana", "Papaya", sep="-")

# No separator
print("Hello", "World", sep="")
# Output: HelloWorld

# Custom separator (newline)
print("First", "Second", "Third", sep="\n")

"""Output:
First
Second
Third"""