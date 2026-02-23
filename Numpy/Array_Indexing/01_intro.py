# Access Array Elements
# Array indexing is the same as accessing an array element.
# You can access an array element by referring to its index number.
# The indexes in NumPy arrays start with 0, meaning that the first element has index 0, and the second has index 1 etc.

import numpy as np

arr = np.array([1,2,344,44,44,2,1])

print(arr[0])
print(arr[1])
print(arr[3])
print(arr[6])
print(arr[7]) # IndexError: index 7 is out of bounds for axis 0 with size 7