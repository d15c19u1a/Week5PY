# Base class
class Animal:
    def move(self):
        print("This animal moves in some way.")

# Subclass for flying animal
class Bird(Animal):
    def move(self):
        print("Flies in the sky")

# Subclass for swimming animal
class Fish(Animal):
    def move(self):
        print("Swims in the water")

# Polymorphism in action
def animal_movement(animal):
    animal.move()

# Example usage
eagle = Bird()
salmon = Fish()
animal = Animal()

animal_movement(eagle)   # Outputs: Flies in the sky
animal_movement(salmon)  # Outputs: Swims in the water
animal_movement(animal)  # Outputs: This animal moves in some way.
