import pandas

my_data = {
    "Cars": ["Bugati", "BMW", "Mahindra", "Volvo"],
    "ratings": [9, 8, 9, 6]
}

analyse_data = pandas.DataFrame(my_data)

print(analyse_data)