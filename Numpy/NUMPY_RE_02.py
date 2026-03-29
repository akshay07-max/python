import numpy as np

# Numpy version
print(np.__version__)

# Creating numpy array
arr = np.array([12, 13, 14, 15])
print(arr) # [12 13 14 15]

# Numpy array object is called ndarray
print(type(arr)) # <class 'numpy.ndarray'>

# converting python tuple to numpy array
tpl = (12, 22, 33, 44)
con_arr = np.array(tpl)

print(con_arr) # [12 22 33 44]
print(type(con_arr)) # <class 'numpy.ndarray'>

# DIMENSIONAL arrays in numpy

# 0-D array
zr_arr = np.array(0)
print(zr_arr) #  0

# check dimension
print(zr_arr.ndim) # 0

# 1-D arrays
one_arr = np.array([12, 22, 33, 45])
print(one_arr) # [12, 22, 33, 45]

# check dimension
print(one_arr.ndim) # 1

# 2-D arrays (Matrix)
tw_arr = np.array([[12, 22, 11, 33], [122, 133, 144, 155]])
print(tw_arr) #[[ 12  22  11  33]
              #  [122 133 144 155]]

# check dimension
print(tw_arr.ndim) # 2

# 3-D arrays
thr_arr = np.array([[[12, 22, 11], [88, 89, 90]], [[111, 222, 333], [444, 555, 666]]])
print(thr_arr)
