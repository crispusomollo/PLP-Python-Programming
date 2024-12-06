# Base Class: Vehicle
class Vehicle:
    def move(self):
        print("The vehicle moves in some way.")

# Subclass: Car
class Car(Vehicle):
    def move(self):
        print("The car is driving 🚗.")

# Subclass: Plane
class Plane(Vehicle):
    def move(self):
        print("The plane is flying ✈️.")

# Subclass: Boat
class Boat(Vehicle):
    def move(self):
        print("The boat is sailing 🛥️.")

# Subclass: Train
class Train(Vehicle):
    def move(self):
        print("The train is chugging along 🚂.")

# Polymorphism in Action
vehicles = [Car(), Plane(), Boat(), Train()]

for vehicle in vehicles:
    vehicle.move()
