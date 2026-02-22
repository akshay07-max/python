# NumPy is a Python library.

# NumPy is used for working with arrays.

# NumPy is short for "Numerical Python".

# In Python we have lists that serve the purpose of arrays, but they are slow to process.

# NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.

# The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.

# Arrays are very frequently used in data science, where speed and resources are very important.

# Data Science: is a branch of computer science where we study how to store, use and analyze data for deriving information from it.

# Why is NumPy Faster Than Lists?
# NumPy arrays are stored at one continuous place in memory unlike lists, so processes can access and manipulate them very efficiently.

# This behavior is called locality of reference in computer science.

# This is the main reason why NumPy is faster than lists. Also it is optimized to work with latest CPU architectures.

# installing Numpy:
# pip install numpy

import numpy

arr = numpy.array([1, 3,45,6])

print(arr)