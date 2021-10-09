"""
Tic Tac Toe Player
"""

import math

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
    # Remember! X Always gets the first move according to the project PDF.
    player_x = 0
    player_o = 0
    # Counts the number of X's and O's on the board. If there are the same amount of X's and O's,
    # then it will return X. Otherwise, it will return O.
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                player_x += 1
            elif board[i][j] == O:
                player_o += 1
    if player_x == player_o:
        return X
    elif player_x > player_o:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # This loop goes through every space of the board. Every time it finds an empty space, it adds
    # the empty section to the possible_actions list.
    possible_actions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.append((i, j))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board[action[0]][action[1]] = player(board)
    return board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """# horizontal
    for i in range(3):
        if ((board[i][0] == board [i][1] ==board [i][2]) and board[i][0]!= EMPTY):
           if (board[i][1] == X):
            return X
           else:
            return O

           # Column
    for i in range(3):
        if ((board[0][i] == board[1][i]== board[2][i]) and board[0][i]!= EMPTY):
         if (board[1][i] == X):
           return X
         else:
           return O

    #diagonal
    if((board[0][0] == board[1][1]== board[2][2]) and board[0][0] != EMPTY):
         if (board[1][1] == X):
           return X
         else:
           return O

    #diagonal
    elif((board[0][2]==board[1][1]==board[2][0]) and board[0][2]!= EMPTY):
         if (board[1][1] == X):
           return X
         else:
           return O

           #counter check for EMPTY spaces
    count =0
    for i in range(3):
        for j in range(3):
            if board[i][j] != EMPTY:
                count+=1
    if (count == 9):
        return None
    #raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Returns true if anyone has won
    if winner(board) == X or winner(board) == O:
        return True
    # Checks the board for any empty spaces. Returns False if it finds any.
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    return True




def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
   # returns applicable number value for winner.
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0




def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # if the board is terminal, there are no moves to make.
    if terminal(board):
        return None

    action = actions(board)

    #If there's only one move left, then that HAS to be the optimal move.
    if len(action) == 1:
        return action[0]

    #Holds the value of the move you're about to make
    value = 0
    best_value = 0
    #Holds the optimal move
    next_move = []

    # Goes through each move and picks the one with a value of 1
    if player(board) == X:
        for moves in action:
            next_move = minimax(result(board, moves))
            value = max(utility(board), value)
            board[moves[0]][moves[1]] = EMPTY
            if value == 1:
                return moves

    #Goes through each move and picks the one with a value of negative 1
    if player(board) == O:
        for moves in action:
            next_move = minimax(result(board, moves))
            value = min(utility(board), value)
            board[moves[0]][moves[1]] = EMPTY
            if value == -1:
                return moves

    return next_move
