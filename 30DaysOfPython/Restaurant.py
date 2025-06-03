class Restaurant:
    def __init__(self, name, cuisine_type,number_served=0):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = number_served
    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.name.title()} and the cuisine type is {self.cuisine_type.title()}")
    def open_restaurant(self):
        print(f"{self.name.title()} is open now!")
    def set_number_served(self,set_number_served):
        self.number_served = set_number_served

    def increment_number_served(self, increment_number_served):
        self.number_served += increment_number_served

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type, flavors, number_served=0):
        super().__init__(name, cuisine_type, number_served)
        self.flavors = flavors
    def describe_flavors(self):
        print(f"The available flavors at {self.name.title()} are {', '.join(self.flavors)}")

# Testing the code
IceCreamStand = IceCreamStand("The Ice Cream Stand", "Ice Cream", ["vanilla", "strawberry", "chocolate"])
IceCreamStand.describe_restaurant()
IceCreamStand.describe_flavors()