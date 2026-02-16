# Abstraction

# Hide internal details, show only essential features.

# Using abc module:


from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

# Child must implement:
class Car(Vehicle):
    def start(self):
        print("Car started")
