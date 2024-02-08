
from random import randint

class Constraint:
    def __init__(self, var1, var2, d1, d2):
        self.var1 = var1
        self.var2 = var2
        self.d1 = d1
        self.d2 = d2
        self.cost = randint(1,100)