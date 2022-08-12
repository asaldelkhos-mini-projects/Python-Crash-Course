# exercise 9-3
class User:
    """docstring for User."""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"My name is {self.first_name} {self.last_name}")

    def greet_user(self):
        print(f"Hi dear {self.first_name}")

person1 = User('Asal', 'delkhosh')
person1.describe_user()
person1.greet_user()
