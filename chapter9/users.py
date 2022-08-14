# exercise 9-3
class User:
    """docstring for User."""
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(f"My name is {self.first_name} {self.last_name}")

    def greet_user(self):
        print(f"Hi dear {self.first_name}")

    def  inccrement_login_attempts(self):
        self.login_attempts += 1
        print(f"{self.login_attempts}")
        
person1 = User('Asal', 'delkhosh')
person1.describe_user()
person1.greet_user()
person1.inccrement_login_attempts()
person1.inccrement_login_attempts()
