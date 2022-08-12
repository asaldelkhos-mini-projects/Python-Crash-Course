#exercise 9-1

class Restaurant:
    """a simple class that describe the restaurant"""
    def __init__(self, name, cuisine):
        """initialize name and age cuisine"""
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        print(f"Restaurant name is {self.name}.")
        print(f"Restaurant cuisine type is {self.cuisine}")

    def open_restaurant(self):
        print(f"{self.name} is open.")

restaurant = Restaurant('Rezae', 'Iranian food')
restaurant.describe_restaurant()
restaurant.open_restaurant()
