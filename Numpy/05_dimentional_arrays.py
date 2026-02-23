# Dimensions in Arrays
# A dimension in arrays is one level of array depth (nested arrays).

# nested array: are arrays that have arrays as their elements.

import numpy as np

# 0 (zero) dimensional
zrArr = np.array(9)

print(zrArr)


# 1-D array
onArr = np.array([1, 23,444])
print(onArr)

# 2-D array. An array which has 1-D as its element is called 2-D array
twArr = np.array([[12,23, 23], [33, 44, 55]])
print(twArr)

# These are often used to represent matrix or 2nd order tensors.
# NumPy has a whole sub module dedicated towards matrix operations called numpy.mat

# 3-D array 
# An array that has 2-D arrays (matrices) as its elements is called 3-D array.
# These are often used to represent a 3rd order tensor.

trArr = np.array([[[3, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(trArr)

