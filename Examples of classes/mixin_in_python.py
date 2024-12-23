# This is a simple example of mixin in Python
# mixin is a class from which we do not create an instance and is used to add functionality to other classes

class WiFiConnectMixin:
    def connect(self):
        print("You are connected to wifi!")

class FoodMixin:
    def food(self):
        print("You ordered food!")


class Vehicle(object):
    def move(self):
        pass

class Car(Vehicle, WiFiConnectMixin):
    pass

class AirPlane(Vehicle, FoodMixin):
    pass

class MotorCycle(Vehicle):
    pass


car = Car()
airplane = AirPlane()
car.connect()
airplane.food()
