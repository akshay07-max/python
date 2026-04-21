import numpy as np

arr = np.array([12, 32, 42, 53, 11, 12, 34, 12])

duplicates = np.where(arr == 12)
print (duplicates)

for i in duplicates:
    for j in i:
        print(arr[j])

get_evens = np.where(arr%2 == 0)
print(get_evens)

for i in get_evens:
    for j in i:
        print(f"Evens: {arr[j]}") 