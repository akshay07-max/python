import numpy as np

#Replace all even numbers with 0
arr = np.arange(1, 11)

arr[arr % 2 == 0] = 0
print(arr)