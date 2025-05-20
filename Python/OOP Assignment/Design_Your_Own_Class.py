# Base class
class Superhero:
    def __init__(self, name, alias, power_level):
        self.name = name
        self.alias = alias
        self.__power_level = power_level  # Encapsulated attribute

    def introduce(self):
        return f"I am {self.alias}, also known as {self.name}!"

    def get_power_level(self):
        return self.__power_level

    def set_power_level(self, value):
        if 0 <= value <= 100:
            self.__power_level = value
        else:
            print("Invalid power level. Must be between 0 and 100.")

    def use_power(self):
        return f"{self.alias} uses their unique power!"

# Derived class - Speedster
class Speedster(Superhero):
    def __init__(self, name, alias, power_level, max_speed):
        super().__init__(name, alias, power_level)
        self.max_speed = max_speed

    def use_power(self):
        return f"{self.alias} runs at lightning speed: {self.max_speed} km/h!"

# Derived class - Telepath
class Telepath(Superhero):
    def __init__(self, name, alias, power_level, mind_control_strength):
        super().__init__(name, alias, power_level)
        self.mind_control_strength = mind_control_strength

    def use_power(self):
        return f"{self.alias} controls minds with strength {self.mind_control_strength}/10!"

# Creating instances
hero1 = Speedster("Lunga Staa", "The Flash", 95, 3000)
hero2 = Telepath("Qhayiya Smile", "Phoenix", 98, 10)

# Demonstrating polymorphism
heroes = [hero1, hero2]

for hero in heroes:
    print(hero.introduce())
    print(hero.use_power())
    print(f"Power Level: {hero.get_power_level()}")
    print("-" * 45)