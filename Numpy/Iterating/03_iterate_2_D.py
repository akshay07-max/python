import numpy as np

arr= np.array([[122, 323, 434], [233, 223, 643]])

for i in arr:
    print(i) # [122 323 434] [233 223 643] 
    # In a 2-D array it will go through all the rows.

# If we iterate on a n-D array it will go through n-1th dimension one by one.

for x in arr:
    for y in x:
        print(y) # this will give you the actual iterated 2-D array elements one by one.
# like:
# 122
# 323
# 434
# 233
# 223
# 643





