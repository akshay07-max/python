class User:
    def __init__(self):
        self.__password = "secret"   # private

    def get_password(self):
        return self.__password