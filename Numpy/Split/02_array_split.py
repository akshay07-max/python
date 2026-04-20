import numpy as np

arr = np.array([12, 34, 54, 12])

split_it = np.array_split(arr, 2)

print(split_it)
# Note: The return value is a list containing two arrays.