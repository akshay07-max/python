import numpy as np

# iterating 1-D array
one_d = np.array(["Apple", "Papaya", "Banana", "Orange"])

# for f in one_d:
#     print(f)

# iterating 2-D array
two_d = np.array([[12, 44, 53, 54], [23, 12, 43, 3]])

# for x in two_d:
#     for n in x:
#         print(n)


# iterating 3-D array
three_d = np.array([[[12, 43, 12, 34], [123, 432, 421, 432]], [[1234, 2342, 4212, 3422], [6534, 7534, 2322, 6432]]])

# for i in three_d:
#     for x in i:
#         for num in x:
#             print(num)


# iterating using nditer

for p in np.nditer(one_d):
    print(p)
