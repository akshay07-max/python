import numpy as np

original_array = np.array([12, 34, 55])

copy_arr = original_array.copy()

copy_arr[0] = 900

print(original_array) # nothing will be changes
print(copy_arr) 