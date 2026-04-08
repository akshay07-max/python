# What if a Value Can Not Be Converted?
import numpy as np

# arr = np.array(['a', '3', '4'], dtype="i")  # gives value error.

# print(arr.dtype)


arr_any = np.array([12, "Apple"]) # 12 is converted to string
print(arr_any)
print(arr_any.dtype) # unicode string