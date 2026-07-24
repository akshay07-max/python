# Read JSON
# Big data sets are often stored, or extracted as JSON.

# JSON is plain text, but has the format of an object, and is well known in the world of programming, including Pandas.

import pandas as pd

get_json = pd.read_json("pandas\data.json")

print(get_json)