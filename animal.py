class Animal(object):
    def __init__(self, name: str, species: str):
        self.name = name
        self.species = species

    def make_sound(self):
        print("some generic animal sound")


class Mammal(Animal):
    def __init__(self, name: str, species: str, num_legs: int):
        super().__init__(name, species)
        self.num_legs = num_legs

    def make_sound(self):
        print("some generic mammal sound")


class Dog(Mammal):
    def __init__(self, name: str, species: str, num_legs, breed: str):
        super().__init__(name, species, num_legs)
        self.breed = breed

    def make_sound(self):
        print("woof! woof!")


animal = Animal("generic", "unknown")
mammal = Mammal("generic", "unknown", 4)
dog = Dog("buddy", "cans", 4, "labrador")
dog.make_sound()
animal.make_sound()
print(animal.name)



