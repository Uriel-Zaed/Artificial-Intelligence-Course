
import random 

from state import State

N = 3 # Must be odd

def dArr_to_2dArr(arr: list):
    board = [[0 for x in range(N)] for y in range(N)]
    k = 0
    for i in range(N):
        for j in range(N):
            board[i][j] = arr[k]
            k += 1
    return board
        


def get_solvable_board():
    num_list = [i for i in range(0,9)]
    is_solvable = False
    while(not is_solvable):
        random.shuffle(num_list)
        if getInvCount(num_list)%2 == 1:
            is_solvable = True
    return num_list


def getInvCount(arr):
    inv_count = 0
    for i in range(N * N - 1):
        for j in range(i + 1,N * N):
            if (arr[j] and arr[i] and arr[i] > arr[j]):
                inv_count+=1
    return inv_count

goal_board_1d = [i for i in range(1,9)]
goal_board_1d.append(0)
goal_board = dArr_to_2dArr(goal_board_1d)
goal_state = State(goal_board)
goal_state.print()

board = get_solvable_board()
board = dArr_to_2dArr(board)
initial_state = State(board)
initial_state.print()