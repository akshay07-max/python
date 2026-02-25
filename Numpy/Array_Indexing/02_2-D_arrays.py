# To access elements from 2-D arrays we can use comma separated integers representing the dimension and the index of the element.

# Think of 2-D arrays like a table with rows and columns, where the dimension represents the row and the index represents the column.

import numpy as np

arr = np.array([[12, 223,33], [21, 32, 42]])

getInd = arr[1, 0]

print(getInd)