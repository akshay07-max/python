import pandas as pd

data = {
    "cate": [122, 534, 543, 654],
    "dt": ["Apple", "Banana", "Parrot", "Coconut"]
}

con_frame = pd.DataFrame(data, index = ["A", "B", "C", "D"])

print(con_frame)

ab = con_frame.loc[["A", "B"]]

print(ab)   