class Animal:
    def __init__(self, animal, leg_number, sound):
        self.name = animal
        self.leg = leg_number
        self.sound = sound
    def features(self):
        print(self.name, "has", self.leg, "legs and sounds", self.sound)


class Cats(Animal):
    pass


cat = Cats("Mia", "4", "meow")
cat2 = Cats("Minerva", "3", "mew")  # Minerva lost her 1 leg in a car accident
cat.features()
cat2.features()


class Dogs(Animal):
    pass


dog = Dogs("Köpüş", "4", "woof-woof")
dog2 = Dogs("Tosuncuk", "4", "ruff-ruff")
dog.features()
dog2.features()
