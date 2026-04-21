import numpy as np

ar = np.array([12, 23, 44, 13])

x = np.searchsorted(ar, 13)

# print(x)

sorted_arr = []

for i in ar:
    pos = np.searchsorted(sorted_arr, i)
    sorted_arr.insert(pos, int(i))

print(sorted_arr)



