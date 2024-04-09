
from node import Node
from problem import Problem
import copy

class BranchAndBound_FC:
    def __init__(self, problem:Problem):
        self.problem = problem
        self.root = Node('root')
        self.UB = 1000000
        self.sol_UB = None

    def solver(self):
        order = self.problem.variables
        for o in order:
            self.root.invalid_domains[o] = []
        queue = [self.root]
        
        while(len(queue)>0):
            current_node = queue.pop(0)
            current_assignmets = self.get_assignments(current_node)

            future_variables = self.get_future_variables(order, current_assignmets)            
            is_cn_valid = self.forward_checking(current_node, current_assignmets, future_variables)

            if is_cn_valid:
                if current_node.varID == 'root':
                        child_varID = order[0]
                else:
                    index_order = order.index(current_node.varID)
                    child_varID = order[index_order + 1] # next var id
                for d in self.remain_domain(current_node.invalid_domains, child_varID):
                    child_cost = current_node.cost + self.problem.get_child_cost(child_varID, d, current_assignmets)
                    if child_cost >= self.UB: # Pruning
                        continue
                    child = Node(child_varID, current_node, d, child_cost)
                    child.invalid_domains = copy.deepcopy(current_node.invalid_domains)
                    if order.index(child_varID) == len(order)-1: # is leaf
                        if child_cost < self.UB: # update upper bound
                            self.UB = child_cost
                            self.sol_UB = self.get_assignments(child) # update best assignment
                            continue
                    queue.insert(0,child)
    
    def forward_checking(self, current_node, current_assignmets, future_variables):
        LB = current_node.cost
        for f_v in future_variables:
            min_cost_f_v = 10000000
            for d in self.remain_domain(current_node.invalid_domains, f_v):
                assigment_cost = self.problem.get_child_cost(f_v, d, current_assignmets)
                if assigment_cost < min_cost_f_v:
                    min_cost_f_v = assigment_cost
                if LB + assigment_cost > self.UB:
                    if not d in current_node.invalid_domains[f_v]:
                        current_node.invalid_domains[f_v].append(d)
            LB += min_cost_f_v
            if LB > self.UB:
                return False # Current Node Assigment invalid
        return True
                
    
    def remain_domain(self, invalid_domain, var):
        remain_domain = []
        for d in self.problem.Domain:
            if not d in invalid_domain[var]:
                remain_domain.append(d)
        return remain_domain

    
    def get_future_variables(self, order, current_assignmets):
        future_variables = []
        for o in order:
            if not o in current_assignmets.keys():
                future_variables.append(o)
        return future_variables


    def get_assignments(self, node: Node):
        assigments = {}
        while(node.parent != None):
           assigments[node.varID] = node.assignment
           node = node.parent
        return assigments 
        