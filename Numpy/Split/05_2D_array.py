# Use the same syntax when splitting 2-D arrays.

# Use the array_split() method, pass in the array you want to split and the number of splits you want to do.

import numpy as np

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr = np.array_split(arr, 3)

# print(newarr)
# print(newarr[0])

# The example above returns three 2-D arrays.

# Let's look at another example, this time each element in the 2-D arrays contains 3 elements.

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3)

# print(newarr)

# The example above returns three 2-D arrays.

# In addition, you can specify which axis you want to do the split around.

# The example below also returns three 2-D arrays, but they are split along the column (axis=1).

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3, axis=1)

print(newarr)