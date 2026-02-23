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
