# Base class
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement the move() method")

# Subclasses with different implementations of move()

class Car(Vehicle):
    def move(self):
        return "Driving on the road 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying in the sky ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing through water 🚤"

class Bicycle(Vehicle):
    def move(self):
        return "Pedaling on the bike lane 🚴"

# Create instances of each subclass
vehicles = [Car(), Plane(), Boat(), Bicycle()]

# Demonstrate polymorphism
for v in vehicles:
    print(v.move())