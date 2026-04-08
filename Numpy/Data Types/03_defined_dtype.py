import numpy as np


# Creating Arrays With a Defined Data Type
# We use the array() function to create arrays, this function can take an optional argument: dtype that allows us to define the expected data type of the array elements:
arr = np.array([12,3, 44, 55], dtype="S")

print(arr.dtype)

# For i, u, f, S and U we can define size as well.