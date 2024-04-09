


class Node:
    def __init__(self, varID, parent=None, assignment=None, cost=0):
        self.varID = varID
        self.parent = parent
        self.assignment = assignment
        self.cost = cost
        self.invalid_domains = {}
