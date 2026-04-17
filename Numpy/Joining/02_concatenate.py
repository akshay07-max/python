import numpy as np

arr1 = np.array([12, 23, 43, 112])

arr2 = np.array(["12", "232", "43", "323"])

join_them = np.concatenate(arr1, arr2)
print(join_them)

# print(arr2.dtype)
# print(arr2)