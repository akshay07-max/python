# To access elements from 3-D arrays we can use comma separated integers representing the dimensions and the index of the element.
import numpy as np

three_d_array = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

getInd = three_d_array[1, 0, 2]

print(getInd)

# so our 3-D array has 2 elements of 2-d arrays, so when we are accessing the element of the array 1 is the second element of 3-D array which is:[[7, 8, 9], [10, 11, 12]]. 
# 0 means the 1st element of the 2-D array which is: [7, 8, 9]. and the 2 is the final element of our array which is 2.


# Example Explained
# arr[0, 1, 2] prints the value 6.

# And this is why:

# The first number represents the first dimension, which contains two arrays:
# [[1, 2, 3], [4, 5, 6]]
# and:
# [[7, 8, 9], [10, 11, 12]]
# Since we selected 0, we are left with the first array:
# [[1, 2, 3], [4, 5, 6]]

# The second number represents the second dimension, which also contains two arrays:
# [1, 2, 3]
# and:
# [4, 5, 6]
# Since we selected 1, we are left with the second array:
# [4, 5, 6]

# The third number represents the third dimension, which contains three values:
# 4
# 5
# 6
# Since we selected 2, we end up with the third value:
# 6

