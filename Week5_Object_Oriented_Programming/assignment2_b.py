# Base Class: Animal
class Animal:
    def move(self):
        print("This animal moves in some way.")

# Subclass: Bird
class Bird(Animal):
    def move(self):
        print("The bird is flying 🐦.")

# Subclass: Fish
class Fish(Animal):
    def move(self):
        print("The fish is swimming 🐟.")

# Subclass: Snake
class Snake(Animal):
    def move(self):
        print("The snake is slithering 🐍.")

# Subclass: Cheetah
class Cheetah(Animal):
    def move(self):
        print("The cheetah is running 🐆.")

# Polymorphism in Action
animals = [Bird(), Fish(), Snake(), Cheetah()]

for animal in animals:
    animal.move()
