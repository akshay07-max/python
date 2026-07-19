import pandas as pd

# A pandas "Series" is like an column in table.
# It hold one dimensional data of any type.

my_data = [1234, 5423, 3421]

get_series = pd.Series(my_data)
print(get_series)


# Labels:
# The label are basically a index of the data (If nothing is specified). The index starts form 0, 1 etc.
# The label can be used to access a specified element.

