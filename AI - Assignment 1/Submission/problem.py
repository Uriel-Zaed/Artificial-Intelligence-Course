
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
        self.counter_constrainted = {v:[] for v in self.variables}
        self.constrains = self.get_constraints()
        self.CC = 0


    def get_most_constrainted_var(self, future_variables, current_assignmets_keys: list):
        counter_constraint = self.counter_constrainted.copy() # copy dic
        for c_a_v in current_assignmets_keys: # for delete all var assignment that used already
            del counter_constraint[c_a_v]
        for cc in counter_constraint.keys(): # for delete var in cc's that that used already
            for var in current_assignmets_keys:
                if var in counter_constraint[cc]:
                    counter_constraint[cc].remove(var)
        max_constrainted = future_variables[0]
        for cc in counter_constraint.keys(): # find max constrainted var
            if len(counter_constraint[cc]) > len(counter_constraint[max_constrainted]):
                max_constrainted = cc
        return max_constrainted

    def CC_reset(self):
        self.CC = 0

    def get_constraints(self):
        constrains = []
        for var1 in range(self.N):
            for var2 in range(var1+1,self.N):
                if random.random() < self.p1:
                    constrains.extend(self.set_binary_constraints(self.variables[var1], self.variables[var2]))
                    self.counter_constrainted[self.variables[var1]].append(self.variables[var2])
                    self.counter_constrainted[self.variables[var2]].append(self.variables[var1])
        
        return constrains

    def set_binary_constraints(self, var1, var2):
        constarints = []
        for d1 in self.Domain:
            for d2 in self.Domain:
                if random.random() < self.p2:
                    constarints.append(Constraint(var1,var2,d1,d2,random.randint(1,100)))
                else:
                    constarints.append(Constraint(var1,var2,d1,d2,0))
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
            elif c.var1 == var and c.d1 == d:
                relevant_constrains.append(Constraint(var1=c.var2,d1=c.d2,var2=c.var1,d2=c.d1,cost=c.cost))
        return relevant_constrains

