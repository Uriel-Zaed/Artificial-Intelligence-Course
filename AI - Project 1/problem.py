
import random
import string

from constraint import Constraint

class Problem:
    def __init__(self, N, D, p1, p2):
        self.N = N # Number of Variables
        self.variables = ['X'+str(i) for i in range(1,N+1)]
        self.D = D # Domain size
        self.Domain = list(string.ascii_lowercase[:D])
        self.p1 = p1 # Density probabilty 
        self.p2 = p2 # Tightness probabilty
        self.constrains = self.get_constraints()
        self.CC = 0

    def get_constraints(self):
        constrains = []
        for var1 in range(self.N):
            for var2 in range(var1+1,self.N):
                if random.random() < self.p1:
                    constrains.extend(self.set_binary_constraints(self.variables[var1], self.variables[var2]))
        
        return constrains

    def set_binary_constraints(self, var1, var2):
        constarints = []
        for d1 in self.Domain:
            for d2 in self.Domain:
                if random.random() < self.p2:
                    constarints.append(Constraint(var1,var2,d1,d2))
        return constarints
    
    def get_child_cost(self, var, d, assigments):
        relevant_constrains = self.get_rellavant_constraints(var, d)
        cost = 0

        for v in assigments.keys():
            for r_c in relevant_constrains:
                if r_c.var1 == v and r_c.d1 == assigments[v]:
                    cost += r_c.cost
                    self.CC += 1
        
        return cost

    def get_rellavant_constraints(self, var, d):
        relevant_constrains = []
        for c in self.constrains:
            if c.var2 == var and c.d2 == d:
                relevant_constrains.append(c)
        return relevant_constrains
        
        

