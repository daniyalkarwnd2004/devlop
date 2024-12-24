# Create an example of polymorphism in Python

class Animal(object):
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def info(self):
        print(f"hello, my name is: {self.name} and i am color: {self.color}")

    def make_sound(self):
        print("animal :)")


class Cut(Animal):
    def __init__(self, name, color):
        super().__init__(name, color)

    def make_sound(self):
        print("mow...")


class Cow(Animal):
    def __init__(self, name, color):
        super().__init__(name, color)

    def info(self):
        print(f"hello, my name is: {self.name} and i am color: {self.color}")

    def make_sound(self):
        print("moo...")


def main():
    cut = Cut("jac", "red")
    cow = Cow("cowe", "black")
    for animal in [cut, cow]:
        animal.info()
        animal.make_sound()

if __name__ == "__main__":
    main()