class Outer:
    def __init__(self, name):
        self.name = name

    class Inner:
        def __init__(self, name):
            self.name = name

        def display(self):
            return self.name
        
c1 = Outer("Akshay")

print(c1)