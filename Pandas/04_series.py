import pandas as pd

categories = {
    "data1": 420,
    "data2": 695,
    "data3": 983
}

my_data = pd.Series(categories)
print(my_data)

print(my_data["data1"]) # the keys becomes the labels

# If i wanted to select multiple Items
get_more = pd.Series(categories, index=["data1", "data2"])

print(get_more)