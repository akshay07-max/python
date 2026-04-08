# Converting Data Type on Existing Arrays

import numpy as np

# The best way to change the data type of an existing array, is to make a copy of the array with the astype() method.

# The astype() function creates a copy of the array, and allows you to specify the data type as a parameter.

# The data type can be specified using a string, like 'f' for float, 'i' for integer etc. or you can use the data type directly like float for float and int for integer.


# Change data type from float to integer by using 'i' as parameter value:
arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i') # int32
# newarr = arr.astype('i4') # int32
# newarr = arr.astype('i8') # int64

print(newarr)
print(newarr.dtype)


# Change data type from float to integer by using int as parameter value:
arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype(int)

print(newarr)
print(newarr.dtype)




# Change data type from integer to boolean:
arr = np.array([1, 0, 3])

newarr = arr.astype(bool)

print(newarr)
print(newarr.dtype)