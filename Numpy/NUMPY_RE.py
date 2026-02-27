import numpy as np

arr = np.array([23, 13, 11, 22, 26])

# print(arr)

# element accessing
# print(arr[0])
# print(arr[1])
# print(arr[2])
# print(arr[3])
# print(arr[-1])

# Dimentional arrays

# 0-D
zr_d = np.array(89)
# print(zr_d)
# print(np.ndim(zr_d))

# 1-D 
on_d = np.array([12,13, 14])
# print(on_d)
# print(np.ndim(on_d))

# 2-D 
tw_d = np.array([[12, 23, 43, 12, 23], [11, 23, 44, 55, 12]])
# print(tw_d)
print(np.ndim(tw_d))

print(tw_d[1, 0])
print(tw_d[0, 3])