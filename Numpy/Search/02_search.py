import numpy as np

arr = np.array([12, 32, 42, 53, 11, 12, 34, 12])

duplicates = np.where(arr == 12)
print (duplicates)

