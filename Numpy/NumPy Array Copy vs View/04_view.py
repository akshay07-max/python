import numpy as np

arr = np.array(["Apple", "Banana", "Orange", "Grapes", "Watermelon"])

arr_view = arr.view()
print(arr_view) # ['Apple' 'Banana' 'Orange' 'Grapes' 'Watermelon']

# make changes in arr_view
arr_view[0] = "Onion"
print(arr_view) # ['Onion' 'Banana' 'Orange' 'Grapes' 'Watermelon']
print(arr) # the original array get changed: ['Onion' 'Banana' 'Orange' 'Grapes' 'Watermelon']

# conclusion: When you change anything with view the original array get affected unlike copy.

# make changes in original array.
arr[2] = "Tomato"
print(arr)
print(arr_view)