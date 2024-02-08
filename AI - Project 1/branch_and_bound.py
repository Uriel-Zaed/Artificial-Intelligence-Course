
from node import Node
from problem import Problem

class BranchAndBound:
    def __init__(self, problem:Problem):
        self.problem = problem
        self.root = Node('root')
        self.UB = 1000000
        self.sol_UB = None

    def solver(self):
        queue = [self.root]
        order = self.problem.variables
        
        while(len(queue)>0):
            current_node = queue.pop(0)
            current_assignmets = self.get_assignments(current_node)
            
            for d in self.problem.Domain:
                if current_node.varID == 'root':
                    child_varID = order[0]
                else:
                    index_order = order.index(current_node.varID)
                    child_varID = order[index_order + 1] # next var id
                child_cost = current_node.cost + self.problem.get_child_cost(child_varID, d, current_assignmets)
                if child_cost >= self.UB: # Pruning
                    continue
                child = Node(child_varID, current_node, d, child_cost)
                if order.index(child_varID) == len(order)-1: # is leaf
                    if child_cost < self.UB: # update upper bound
                        self.UB = child_cost
                        self.sol_UB = self.get_assignments(child) # update best assignment
                        continue
                queue.insert(0,child)


    def get_assignments(self, node: Node):
        assigments = {}
        while(node.parent != None):
           assigments[node.varID] = node.assignment
           node = node.parent
        return assigments 
        