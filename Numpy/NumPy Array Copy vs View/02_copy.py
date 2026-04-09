import numpy as np

original_arr = np.array([23, 44, 66, 77, 88])

copy_arr = original_arr.copy()

original_arr[3] = 900  # changing element at position 3.

print(original_arr)
print(copy_arr)