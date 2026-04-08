# check data type of an array

import numpy as np

arr = np.array([12, 33, 44, 55])

print(arr.dtype)

if arr.dtype == "int64":
    print("Array integer hai!!")

else:
    print("Array hi hai!!")


