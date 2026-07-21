# Data sets in Pandas are usually multi-dimensional tables, called Dataframes.
#series is like a column of the table, But the Dataframe is an Table.

import pandas as pd

data = {
    "categories": [12, 43, 32, 53],
    "data": [212, 343, 546, 321]
}

get_frame = pd.DataFrame(data)
print(get_frame)