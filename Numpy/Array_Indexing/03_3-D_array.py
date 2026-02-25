import numpy as np

three_d_array = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

getInd = three_d_array[1, 0, 2]

print(getInd)

# so our 3-D array has 2 elements of 2-d arrays, so when we are accessing the element of the array 1 is the second element of 3-D array which is:[[7, 8, 9], [10, 11, 12]]. 
# 0 means the 1st element of the 2-D array which is: [7, 8, 9]. and the 2 is the final element of our array which is 2.