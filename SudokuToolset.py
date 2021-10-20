BLANK = 0
DIGITS = set(range(1,10))
from collections import Counter

def get_row(board, row):
    return set(board[row])

def is_valid(row):
    Counter(row) == Counter(DIGITS)

def get_col(board, col):
    return set([board[row][col] for row in range(9)])

def get_box(board, row, col):
    i, j= row // 3, col // 3
    sqr = [row[j*3:j*3+3] for row in board[i*3:i*3+3]] #sqr as list of rows
    return set([x for sub in sqr for x in sub]) #flattening

def get_viable_vertical(board, row) -> set:
    return DIGITS - get_row(board, row)

def get_viable_horizontal(board, col) -> set:
    return DIGITS - get_col(board, col)

def get_viable_box(board, row, col) -> set:
    return DIGITS - get_box(board, row, col)

def get_viable_digits(board, row, col) -> set:
    return get_viable_vertical(board, row) & get_viable_horizontal(board, col) & get_viable_box(board, row, col)

def find_blank(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == BLANK:
                return i, j
    return None, None
            #return (i, j) if board[i][j] == BLANK else (None, None)

def fill(board):
    x, y = find_blank(board)
    if x is None:
        return True
    
    for d in DIGITS:
        if d in get_viable_digits(board, x, y):
            board[x][y] = d
            if fill(board):
                return True
            board[x][y] = BLANK
    return False

def printboard(board):
    for row in board:
        for i in row:
            print(i, end =" ")
        print()
