import random

class Dice:
    def __init__(self,sides):
        self.sides = sides
    def __call__(self):
        return random.randint(1,self.sides)
