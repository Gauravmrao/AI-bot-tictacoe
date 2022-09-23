"""
Tic Tac Toe Player
"""

import math
from sys import base_exec_prefix

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
    initial = initial_state()

    if terminal(board) :
        return "over"
    if board == initial:
        return X

    move_counter = 0
    for row in board:
        for cell in row:
            if cell != EMPTY:
                move_counter += 1

    if move_counter % 2 == 0:
        return X
    else:
        return O



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if terminal(board) :
        return "over"
    moves = []
    i = 0
    j = 0
    for row in board:
        j = 0
        for cell in row:
            if cell == EMPTY:
                moves.append((i + 0, j + 0))
            j += 1
        i += 1
    return moves



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    result_board = [[],[],[]]
    counter = 0
    for row in board:
        for cell in row:
            result_board[counter].append(cell)
        counter += 1

    to_add = player(board)
    rowy = action[0]
    celly = action[1]
    result_board[rowy][celly] = to_add
    return result_board


def win_detector(board, symbol):
    if board[0][0] == symbol and board[0][1] == symbol and board[0][2] == symbol:
        return symbol
    elif board[1][0] == symbol and board[1][1] == symbol and board[1][2] == symbol:
        return symbol
    elif board[2][0] == symbol and board[2][1] == symbol and board[2][2] == symbol:
        return symbol
    elif board[0][0] == symbol and board[1][0] == symbol and board[2][0] == symbol:
        return symbol
    elif board[0][1] == symbol and board[1][1] == symbol and board[2][1] == symbol:
        return symbol
    elif board[0][2] == symbol and board[1][2] == symbol and board[2][2] == symbol:
        return symbol
    elif board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol:
        return symbol
    elif board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol:
        return symbol
    else:
        return None


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if win_detector(board, X) == X:
        return X
    elif win_detector(board, O) == O:
        return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) != None:
        return True
    filler = True
    for row in board:
        for cell in row:
            if cell == EMPTY:
                filler = False
    return filler


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    moves = actions(board)
    
    



    
    
    
    v_values = []
    counter = 0

    for move in moves:
        if player(board) == X:
            v_values.append(min_value(result(board,moves[counter])))
        else:
            v_values.append(max_value(result(board,moves[counter])))
        counter += 1

    if player(board) == O:
        mini = min(v_values)
        location = v_values.index(mini)
        return moves[location]
    elif player(board) == X:
        maxi = max(v_values)
        locationi = v_values.index(maxi)
        return moves[locationi]


