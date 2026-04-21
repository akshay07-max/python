import numpy as np

ar = np.array([12, 23, 44, 13])

x = np.searchsorted(ar, 13)

print(x)