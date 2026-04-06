# Numpy cheat sheet-2
# Accessing Index In Numpy

import numpy as np

# same as other programming languages in python also the indexing starts from zero
# 1-D Array
one_d_arr = np.array([12, 11, 23, 31])
# print(one_d_arr[2]) # 23

# 2-D Array
tw_d_array = np.array([[12, 33, 44], [32, 44,21]])
# print(tw_d_array[1, 2])  # 21

# 3-D array
thr_d_array = np.array([[[12, 33, 44, 55, 77], [45, 65, 76, 87, 21]], 
                        [[56, 877, 999, 888, 767], [885, 643, 988, 887, 998]]])
# print(thr_d_array[1, 1, 0]) # 885


# Array Slicing
# Slicing in python means taking elements from one given index to another given index.
# We pass slice instead of index like this: [start:end].
# We can also define the step, like this: [start:end:step].
# If we don't pass start its considered 0
# If we don't pass end its considered length of array in that dimension
# If we don't pass step its considered 1


arr = np.array([12, 23, 34, 45, 56, 67, 78])
print(arr[1:4]) # [23 34 45]
# Note: The result includes the start index, but excludes the end index.

