import numpy as np


# arr = np.array([12, 23, 43, 45, 21])
# arr = np.array([[12, 32, 434, 55, 12], [12, 23, 43, 45, 21]])

arr = np.array([[[122, 331, 222], [2223, 343, 122]], [[122, 321, 332], [321, 322, 122]], [[123, 223, 432], [3232, 4343, 5453]]])

get_shape = arr.shape

print(get_shape) # (3, 2, 3) for 3-D array 3 is the elements of outer most dimension, 2 is 1 step inner, the elements of 2-D array which is inside, and so on.