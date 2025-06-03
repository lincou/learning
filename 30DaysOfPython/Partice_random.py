import random
class Die:
    def __init__(self,sides=6):
        self.sides = sides
    def roll(self,num_rolls=1):
        result = []
        for i in range(num_rolls):
            result.append(random.randint(1,self.sides))
        return result
    
d1 = Die()
d2 = Die(10)
d3 = Die(20)

print(d1.roll(10))
print(d2.roll(10))
print(d3.roll(10))