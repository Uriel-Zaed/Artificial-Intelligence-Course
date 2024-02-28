

class State():
    def __init__(self, board):
        self.board = board

    def print(self):
        for i in self.board:
            for j in i:
                if j == 0:
                    print(" ,", end = ' ')
                else:
                    print(str(j)+",", end = ' ')
            print()

    def __eq__(self, __value) -> bool:
        return self.board == __value.board
    