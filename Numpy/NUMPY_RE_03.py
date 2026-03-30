# Numpy cheat sheet-2
# Indexing In Numpy

import numpy as np

# same as other programming languages in python also the indexing starts from zero
# 1-D Array
one_d_arr = np.array([12, 11, 23, 31])
print(one_d_arr[2]) # 23

# 2-D Array
tw_d_array = np.array([[12, 33, 44], [32, 44,21]])
print(tw_d_array[1, 2])  # 21

# 3-D array
thr_d_array = np.array([[[12, 33, 44, 55, 77], [45, 65, 76, 87, 21]], 
                        [[56, 877, 999, 888, 767], [885, 643, 988, 887, 998]]])
print(thr_d_array[1, 1, 0]) # 885

