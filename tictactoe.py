"""
Tic Tac Toe Player
"""

import math
import copy
X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    countX = 0
    countO = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == X:
                countX += 1
            if board[row][col] == O:
                countO += 1
    if countX == countO:
        return X
    else:
        return O


    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    possible_action = set()
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == EMPTY:
                possible_action.add((row, col))
    return possible_action

    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Not valid action")

    (x, y) = action
    if x < 0 or x >= len(board) or y < 0 or y > len(board[0]):
        raise IndexError()

    new_board = copy.deepcopy(board)
    new_board[x][y] = player(board)
    return new_board
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if check_row(board, X) or check_column(board, X) or check_top_to_bottom_diagonal(board, X) or check_bottom_to_top_diagonal(board, X):
        return X
    elif check_row(board, O) or check_column(board, O) or check_top_to_bottom_diagonal(board, O) or check_bottom_to_top_diagonal(board, O):
        return O
    else: 
        return None
    raise NotImplementedError

def check_row(board, player):
    for row in range(len(board)):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True 
    return False

def check_column(board, player): 
    for col in range(len(board)):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    return False

def check_top_to_bottom_diagonal(board, player):
    row = 0
    col = 0
    count = 0
    while row < len(board):
        if board[row][col] == player:
            count += 1
        row += 1
        col += 1
    if count == len(board):
        return True
    return False

def  check_bottom_to_top_diagonal(board, player):
    row = 2
    col = 0
    count = 0
    while col < 3:
        if board[row][col] == player:
            count += 1
        row = row - 1
        col += 1
    if count == 3:
        return True
    return False

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O:
        return True
    count = 0
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] != EMPTY:
                count += 1
    if count == (len(board) * len(board[0])):
        return True
    return False
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board) == True:
        if winner(board) == X:
            return 1
        return -1
    else:
        return 0
    raise NotImplementedError



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    elif player(board) == X:
        if board == [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]:
            return (1,1)
        v = float("-inf")
        final_act = ()
        for action in actions(board):
            val = (min_value(result(board, action)), action)
            if val[0] > v:
                v = val[0]
                final_act = (v, val[1])
        return final_act[1]

    elif player(board) == O:
        v = float("inf")
        final_act = ()
        for action in actions(board):
            val = (max_value(result(board, action)), action)
            if val[0] < v:
                v = val[0]
                final_act = (v, val[1])
        return final_act[1]

    raise NotImplementedError

def max_value(board):
    if terminal(board):
        return utility(board)
    v = float("-inf")
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = float("inf")
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v



