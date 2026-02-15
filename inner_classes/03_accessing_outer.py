# Inner classes in Python do not automatically have access to the outer class instance.

# If you want the inner class to access the outer class, you need to pass the outer class instance as a parameter:

class Outer:
  def __init__(self):
    self.name = "Emil"

  class Inner:
    def __init__(self, outer):
      self.outer = outer

    def display(self):
      print(f"Outer class name: {self.outer.name}")

outer = Outer()
inner = outer.Inner(outer)
inner.display()