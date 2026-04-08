# check data type of an array

import numpy as np

arr = np.array([12, 33, 44, 55])

print(arr.dtype)

if arr.dtype == "int64":
    print("Array integer hai!!")

else:
    print("Array hi hai!!")


# creating array of strings
strArr = np.array(["Apple", "Jamun", "Orange", "Papaya"])

print(strArr.dtype)


print(arr.dtype)

if strArr.dtype == "int64":
    print("Array integer hai!!")

else:
    print("Array kuch or hi hai!!")