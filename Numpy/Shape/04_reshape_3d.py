import numpy as np

# 1-D to 3-D

# Convert the following 1-D array with 12 elements into a 3-D array.
# The outermost dimension will have 2 arrays that contains 3 arrays, each with 2 elements:
arr = np.array([12, 33, 44, 55, 66, 22, 33, 44, 55, 77, 88, 56])

new_arr = arr.reshape(2, 3, 2)

print(new_arr)