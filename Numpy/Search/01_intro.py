# Searching Arrays
# You can search an array for a certain value, and return the indexes that get a match.

# To search an array, use the where() method.

import numpy as np

arr = np.array([122, 32, 312, 122, 322, 122, 34,  122])

duplicates = np.where(arr == 122)

print(duplicates) # (array([0, 3, 5, 7]),)
# Which means that the value 122 is present at index 0, 3, 5 and 7.
