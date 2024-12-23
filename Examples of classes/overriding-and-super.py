# Solving the overriding problem using the super function in Python
# A simple example is made
# Note that it is not a project, it is just code from classes to review topics

class User(object):
    show_users = []

    def __init__(self, name, user_name, password):
        self.name = name
        self.user_name = user_name
        self.password = password
        self.show_users.append([self.name, self.user_name, self.password])

    def __repr__(self):
        return f"name :{self.name} and user_name: {self.user_name}"

    def __str__(self):
        return f"name: {self.name}"


class Behavior(User):
    def add_behavior(self, behav:"ordering"):
        return f"hello my name is: {self.name} my name and behavior is: {behav}"

class Admin(User):
    def __init__(self, name, user_name, password, phone):
        super().__init__(name, user_name, password)
        self.phone = phone

user = User("dani", "dani2003", "123456")
behavior = Behavior("dani", "dani2003", "123456")
print(behavior.add_behavior("love to learn"))
admin = Admin("dani", "dani2003", "123456", "0933333")
print(admin.phone)

