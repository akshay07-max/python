# As you can see from the result above, the DataFrame is like a table with rows and columns.

# Pandas use the loc attribute to return one or more specified row(s)

import pandas as pd

data = {
    "categories": [12, 43, 32, 53],
    "data": [212, 343, 546, 321]
}

get_frame = pd.DataFrame(data)

# print(get_frame.loc[0])

# Note: This example returns a Pandas Series.

print(get_frame.loc[[0,1,2]])