#exercise 9-1

class Restaurant:
    """a simple class that describe the restaurant"""
    def __init__(self, name, cuisine):
        """initialize name and age cuisine"""
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant name is {self.name}.")
        print(f"Restaurant cuisine type is {self.cuisine}")
        print(f"{self.name} is open.")
        print(f"{self.number_served}")

    def update_number_served(self, num):
        self.number_served = num

class IceecreamStand(Restaurant):
        def __init__(self, name, cuisine):
            """initialize attributes of parent class"""
            super.__init__(name, cuisine)
            self.flavors = Flavors_list()

        def Flavors_list(self):
            flavors = ['chocolate', 'vanila', 'coffee', 'stawberry']
            for flavor in flavors:
                print(flavor)

restaurant = IceecreamStand('shad ice cream', 'ice cream')
restaurant.Flavors_list()                
"""
restaurant = Restaurant('Rezae', 'Iranian food')
restaurant.update_number_served(10)
restaurant.describe_restaurant()
"""
