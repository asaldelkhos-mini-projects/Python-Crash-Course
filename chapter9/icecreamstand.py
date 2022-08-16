from restaurant import Restaurant

class IceecreamStand(Restaurant):
        def __init__(self, name, cuisine):
            """initialize attributes of parent class"""
            super().__init__(name, cuisine)

        def flavors_list(self):
            flavors = ['chocolate', 'vanila', 'coffee', 'stawberry']
            for flavor in flavors:
                print(flavor)
print('\n\n')
restaurant2 = IceecreamStand('shad ice cream', 'ice cream')
restaurant2.describe_restaurant()
restaurant2.flavors_list()
