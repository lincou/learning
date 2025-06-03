#while循环练习



# prompt = "\nPlease enter the name of a city you have visited:" 
# prompt += "\n(Enter 'quit' when you are finished.) " 

# city = input(prompt) 
# print(city)
# while True: 
#     city = input(prompt) 
#     if city == 'quit': 
#         break 
#     else: 
#         print(f"I'd love to go to {city.title()}!")

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant_name}")