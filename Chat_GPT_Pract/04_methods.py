class Demo:
    def show(self):
        print("Instance method")


class Demo:
    count = 0

    @classmethod
    def increment(cls):
        cls.count += 1


# Static Method:

# No access to class or instance
class Math:
    @staticmethod
    def add(a, b):
        return a + b
