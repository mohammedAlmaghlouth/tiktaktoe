"""
Tic Tac Toe Player
"""
#I imported copy because I want to copy the results of the board without changing the original board.

import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    # This is the initial state of the board , no one play yet , so it will be empty.
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    
    # to now whos turn , we need to count the numebr of both 'x' and 'o'
    # so that 'x' is always playes first, and when the 'x' and 'o' are equal 
    # then its cleary that its 'x' turn .. 
    
    # creat 'x' & 'o' counting variables with zero because initial state is empty 
    countForX = 0 
    countForO = 0
    
    # now , we need to count number of 'x' & 'o' in the whole board , with nested loop
    
    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column] == X:
                countForX = countForX + 1
            elif board[row][column]==O :
                countForO = countForO + 1
                
    if countForX > countForO:
        return O
    else:
        return X

    #raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    
    # first, we want to create a set that store all avaliable places to move in
    avaliable_places = set()
    
    # then , we will iteraty in each block so that to check if its empty or not
    for row in range(0,len(board)):
        for column in range(0,len(board[0])):
            if board[row][column]==EMPTY:
                avaliable_places.add((row,column))
                
    return avaliable_places
                
    #raise NotImplementedError


def result(board, action):
    
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # so that we do not change the original BOARD... WE COPY IT:
    resultnewBoard = copy.deepcopy(board)
    
    resultnewBoard[action[0]][action[1]] = player(board)
    
    return resultnewBoard

    #raise NotImplementedError
    




    
def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #I WANT TO CHECK ALL THE ROWS 
    
    if all(i == board[0][0] for i in board[0]):
        return board[0][0]
    
    elif all(i == board[1][0] for i in board[1]):
        return board[1][0]
    
    elif all(i == board[2][0] for i in board[2]):
        return board[2][0]
    #I WANT TO CHECK ALL THE COLUMNS
    
    elif board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        return board[0][0]
    
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        return board[0][1]
    
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        return board[0][2]
    
    #I WANT TO CHECK ALL THE DIAGONALS
    
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if (winner(board) == X):
        return True
    
    elif (winner(board) == O):
        return True
        
    for i in range(3):
        
        for j in range(3):
            
            if  board[i][j] == None:
                return False
            
    return True
    


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # from given utilities scores^ wee assign them to given winners
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0
    
    
    #raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    if terminal(board):
        return None
    else:
        
        if player(board) == X:
            value, move = max_Value(board)
            return move
        
        else:
            value, move = min_Value(board)
            return move
        
#TWO HELPER FUNCTIONS FOR minimax: min_Value and max_Value:

def min_Value(board):
    
    if terminal(board):
        return utility(board) , None

    v = float('inf')
    
    move = None
    
    for action in actions(board):
        
        test , act = max_Value(result(board, action))
        
        if test < v:
            v = test
            move = action
            
            if v == -1:
                return v, move

    return v, move
    
#the second helper method.
def max_Value(board):
    
    if terminal(board):
        return utility(board) , None

    v = float('-inf')
    
    move = None
    
    for action in actions(board):

        test , act = min_Value(result(board, action))
        
        if test > v:
            v = test
            move = action
            
            if v == 1:
                return v, move

    return v, move


