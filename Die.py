import random

class Die:
    def __init__(self,n):
        self.numberOfSides = n

    def roll(self):
        return round(random.uniform(1,self.numberOfSides))