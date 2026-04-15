import numpy as np

arr = np.array([12, 32, 22, 22])

shape_it = arr.reshape(4, 1) 

# [[12]
#  [32]
#  [22]
#  [22]]

print(shape_it)