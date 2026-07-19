import pandas as pd

my_data = {
    "Cars": ["Bugati", "BMW", "Mahindra", "Volvo"],
    "ratings": [9, 8, 9, 6]
}

analyse_data = pd.DataFrame(my_data)

print(analyse_data)

print(f"pandas version: {pd.__version__}")