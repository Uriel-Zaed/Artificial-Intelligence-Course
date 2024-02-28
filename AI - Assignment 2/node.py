
class Node():
    def __init__(self, state, parent, g_n, h_n):
        self.state = state
        self.parent = parent
        self.g_n = g_n
        self.h_n = h_n