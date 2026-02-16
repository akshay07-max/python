# Wrapping data + methods together & restricting access.

# Public
# self.name

# Protected (Convention)
# self._salary

# Private
# self.__password



class Bank:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance


# Accessing private directly:
b = Bank(1000)
print(b._Bank__balance)  # Name mangling
