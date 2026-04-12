# Reshaping arrays
# Reshaping means changing the shape of an array.

# The shape of an array is the number of elements in each dimension.

# By reshaping we can add or remove dimensions or change number of elements in each dimension.

import numpy as np

# Convert the following 1-D array with 12 elements into a 2-D array.

# The outermost dimension will have 4 arrays, each with 3 elements:

arr = np.array([1, 3, 4, 5, 6, 7, 9, 8, 90,80, 70, 60])

new_arr = arr.reshape(4, 3) # what it says, create an 2-D array of the given array each having 3 elements in each and will have 4 arrays.

print(new_arr)






