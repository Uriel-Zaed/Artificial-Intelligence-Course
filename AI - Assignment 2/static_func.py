import random 
from state import State

def generate_initial_states(num_of_problems,N):
    inital_states = []  
    for p in range(num_of_problems):
        board = get_solvable_board(N)
        board = dArr_to_2dArr(board,N)
        inital_states.append(State(board))
    return inital_states
    
def generate_goal_state(N):
    goal_board_1d = [i for i in range(1,9)]
    goal_board_1d.append(0)
    goal_board = dArr_to_2dArr(goal_board_1d,N)
    return State(goal_board)

def dArr_to_2dArr(arr: list, N):
    board = [[0 for x in range(N)] for y in range(N)]
    k = 0
    for i in range(N):
        for j in range(N):
            board[i][j] = arr[k]
            k += 1
    return board
        
def get_solvable_board(N):
    num_list = [i for i in range(0,9)]
    is_solvable = False
    while(not is_solvable):
        random.shuffle(num_list)
        if getInvCount(num_list, N)%2 == 0:
            is_solvable = True
    return num_list


def getInvCount(arr, N):
    inv_count = 0
    for i in range(N * N - 1):
        for j in range(i + 1,N * N):
            if (arr[j] and arr[i] and arr[i] > arr[j]):
                inv_count+=1
    return inv_count