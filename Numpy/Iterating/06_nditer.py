import numpy as np

arr = np.array([[123, 432, 423, 556], [121, 432, 564, 455]])

for i in np.nditer(arr):
    print(i)