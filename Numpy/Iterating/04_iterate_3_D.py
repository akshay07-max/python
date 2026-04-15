import numpy as np

arr = np.array([[[12, 32, 43], [12, 33, 53]], [[12, 443, 545], [23, 443, 54]]])

for x in arr:
    print (x)  # it will return two 2D array.


for i in arr:
    for j in i:
        print(j) # it will return four 1-D arrays

for x in arr:
    for y in x:
        for z in y:
            print(z) # see the magic. All individual elements of an 3-D array are there.
 
