
from state import State
from node import Node

class A_Star():
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.root = Node(initial_state, None, 0, self.huer_Man(initial_state))
        self.solution = None

    
    def solve(self):
        frontier = [self.root]
        explored = []

        while(len(frontier) > 0):
            cur_node = frontier.pop(0)

            if cur_node.state == self.goal_state:
                # TODO: self.solution =
                return cur_node
            
            explored = self.add_node_to_explored(cur_node, explored)

            # create list of childs
            child_list = self.get_childs(cur_node)

            for child in child_list:
                if (not self.in_list(child, frontier)) and (not self.in_list(child, explored)):
                    frontier = self.add_node_to_frontier(child, frontier)
                    
                    

            
    def get_childs(self, cur_node):
        pass

    def in_list(self, node, list) -> bool:
        pass
    
    def add_node_to_frontier(self, node, frontier):
        # if have state then check lower cost
        pass
    
    def add_node_to_explored(self, node, explored):
        pass

    # Manhetten dist from each tile to his goal
    def huer_Man(self, state: State):
        sum_h = 0
        for i in len(state.board):
            for j in len(state.board[i]):
                g_i, g_j = self.find_goal_square(state.board[i][i])
                sum_h += self.manhetten_dist(i, j, g_i, g_j)
        return sum_h
    
    def manhetten_dist(self, i, j, g_i, g_j):
        return abs(i-g_i)+abs(j-g_j)
        
    def find_goal_square(self, number):
        for i in len(self.goal_state.board):
            for j in len(self.goal_state.board[i]):
                if self.goal_state.board[i][j] == number:
                    return i, j
        return -1, -1

