# An alternate solution is using hsplit() opposite of hstack()

# Use the hsplit() method to split the 2-D array into three 2-D arrays along columns.

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.hsplit(arr, 3)

print(newarr)

# Note: Similar alternates to vstack() and dstack() are available as vsplit() and dsplit().