from math import hypot


class Point:
    """
    Finds the distance between two points
    >>> p1 = Point(4, 2)
    >>> p2 = Point()

    """
    def __init__(self, x: float = 0, y: float = 0):
        """
        __init__ is for initialization
        :param x: The x value is there by default
        :param y: The y value is there by default
        """
        self.x = x
        self.y = y

    def reset(self):
        """
        It is to reset the values
        :return:Returns the value 0
        """
        self.x = 0
        self.y = 0

    def move(self, x: float, y: float):
        """
        Inserts new values
        :param x: x
        :param y: y
        :return:
        Returns the new value
        """
        self.x = x
        self.y = y

    def discount(self, other: "Point"):
        """
        Finds the distance between two points
        :param other: is equal to the property of p2
        :return: Returns the distance
        """
        return hypot(self.x - other.x, self.y - other.y)


p1 = Point()
print(p1.x)
print(p1.y)
print(help(Point))