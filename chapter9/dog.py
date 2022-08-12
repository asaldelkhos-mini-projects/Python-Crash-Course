class Dog:
    """a simple attempt to model a dog"""

    def __init__(self, name, age):
        """initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """simulate a dog sittig in response to a commad."""
        print(f"{self.name} is sittig.")

    def roll_over(self):
        """simulate a dog rolling over in response to a commad."""
        print(f"{self.name} is rolled over!")

dog_name = input("What is your dog name? ")
dog_age = input("How old is your dog? ")
Dog(dog_name,dog_age)
dog_name.sit()
dog_name.roll_over()
