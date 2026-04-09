import numpy as np

# Make a view, change the original array and display both the arrays

original_array = np.array([122, 333, 322, 544, 655])

x = original_array.view()
print(x)

original_array[3] = 7888

print(original_array)
print(x)