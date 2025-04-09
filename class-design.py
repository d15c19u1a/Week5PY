# Base class
class Planet:
    def __init__(self, name, size_km, distance_from_sun_million_km):
        self.name = name
        self.size_km = size_km
        self.distance_from_sun = distance_from_sun_million_km

    def describe(self):
        print(f"Planet Name: {self.name}")
        print(f"Size: {self.size_km} km in diameter")
        print(f"Distance from Sun: {self.distance_from_sun} million km")

    def orbit(self):
        print(f"{self.name} is orbiting the sun.")

# Subclass using inheritance
class InhabitedPlanet(Planet):
    def __init__(self, name, size_km, distance_from_sun_million_km, population):
        super().__init__(name, size_km, distance_from_sun_million_km)
        self.__population = population  # Encapsulated attribute

    def describe(self):
        super().describe()
        print(f"Population: {self.__population}")

    def support_life(self):
        print(f"{self.name} supports life with a population of {self.__population}.")

# Example usage
earth = InhabitedPlanet("Earth", 12742, 149.6, 8_000_000_000)
earth.describe()
earth.orbit()
earth.support_life()
