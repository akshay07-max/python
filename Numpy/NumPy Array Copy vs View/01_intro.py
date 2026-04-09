# The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.

# The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.

# The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.


# Copy:

# Make a copy, change the original array, and display both arrays:
import numpy as np

arr = np.array([12, 45, 67, 89])

x = arr.copy()

arr[0] = 90

print(arr)
print(x)

# The copy SHOULD NOT be affected by the changes made to the original array.