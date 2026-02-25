import numpy as np

arr = np.array([12, 13, 14, 15, 16])

print(arr[1:4])

# Note: The result includes the start index, but excludes the end index.

# Slice elements from index 4 to the end of the array:
print(arr[4:])

# Slice elements from the beginning to index 4 (not included):
print(arr[:4])