# The point is this is not a project
# It is just a simple example of solving the diamond problem and using mro in Python

class BaseClass(object):
    number_base_class = 0

    def call_func(self):
        print("calling class on BaseClass")
        self.number_base_class += 1


class LeftClass(BaseClass):
    number_left_class = 0

    def call_func(self):
        # The situation where the diamond problem occurs
        # BaseClass.call_func(self)

        # A mode that solves the diamond problem
        super().call_func()
        print("calling class on LeftClass")
        self.number_left_class += 1


class RightClass(BaseClass):
    number_right_class = 0

    def call_func(self):
        # The situation where the diamond problem occurs
        # BaseClass.call_func(self)

        # A mode that solves the diamond problem
        super().call_func()
        print("calling class on RightClass")
        self.number_right_class += 1



class SubClass(LeftClass, RightClass):
    number_sub_class = 0

    def call_func(self):
        # The situation where the diamond problem occurs

        # LeftClass.call_func(self)
        # RightClass.call_func(self)

        # A mode that solves the diamond problem
        super().call_func()
        print("calling class on SubClass")
        self.number_sub_class += 1


sub_class = SubClass()
sub_class.call_func()
# Try it yourself :)