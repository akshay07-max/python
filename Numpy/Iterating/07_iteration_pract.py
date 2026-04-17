import numpy as np

# iterating 1-D array
one_d = np.array(["Apple", "Papaya", "Banana", "Orange"])

for f in one_d:
    print(f)

# iterating 2-D array
two_d = np.array([[12, 44, 53, 54], [23, 12, 43, 3]])

for x in two_d:
    for n in x:
        print(n)