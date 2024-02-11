
from node import Node
from problem import Problem
import random

class BranchAndBound_Hur:
    def __init__(self, problem:Problem):
        self.problem = problem
        self.root = Node('root')
        self.UB = self.create_init_UB()
        self.sol_UB = None
    
    def create_init_UB(self):
        cost = 0
        assigments = {}
        for var1 in self.problem.variables:
            assigments[var1] = random.choice(self.problem.Domain)
        for c in self.problem.constrains:
            if assigments[c.var1] == c.d1 and assigments[c.var2] == c.d2:
                cost += c.cost
                self.problem.CC += 1
        return cost
                  

    def solver(self):
        queue = [self.root]
        # order = self.problem.variables
        
        while(len(queue)>0):
            current_node = queue.pop(0)
            current_assignmets = self.get_assignments(current_node)
            future_vars = self.get_future_variables(self.problem.variables, current_assignmets)
            child_varID = self.problem.get_most_constrainted_var(future_vars,current_assignmets.keys())

            childs = []
            for d in self.problem.Domain:
                child_cost = current_node.cost + self.problem.get_child_cost(child_varID, d, current_assignmets)
                if child_cost >= self.UB: # Pruning
                    continue
                child = Node(child_varID, current_node, d, child_cost)
                if len(future_vars) == 1: # is leaf
                    if child_cost < self.UB: # update upper bound
                        self.UB = child_cost
                        self.sol_UB = self.get_assignments(child) # update best assignment
                        continue
                childs.append(child)
            sorted_childs = self.sort_max_childs(childs)
            for s_c in sorted_childs:
                queue.insert(0,s_c)
        
    def sort_max_childs(self, childs):
        max_index = 0
        for i in range(len(childs)):
            max_index = i
            for j in range(i + 1, len(childs)):
                if childs[j].cost > childs[max_index].cost:
                    max_index = j
            temp = childs[i]
            childs[i] = childs[max_index]
            childs[max_index] = temp
        
        return childs
                

    def get_assignments(self, node: Node):
        assigments = {}
        while(node.parent != None):
           assigments[node.varID] = node.assignment
           node = node.parent
        return assigments 
    
    def get_future_variables(self, order, current_assignmets):
        future_variables = []
        for o in order:
            if not o in current_assignmets.keys():
                future_variables.append(o)
        return future_variables
        