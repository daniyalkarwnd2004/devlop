class Basic(object):
    num_basic = 0

    def call_me(self):
        print("colling Basic")
        self.num_basic += 1


class Lift(Basic):
    num_lift = 0

    def call_me(self):
        super().call_me()
        print("colling Lift")
        self.num_lift += 1


class Right(Basic):
    num_right = 0

    def call_me(self):
        super().call_me()
        print("calling Right")
        self.num_right += 1


class Sub(Lift, Right):
    num_sub = 0

    def call_me(self):
        super().call_me()
        print("calling sub")
        self.num_sub += 1


s = Sub()
s.call_me()
print(s.num_sub, s.num_right, s.num_lift, s.num_basic)
