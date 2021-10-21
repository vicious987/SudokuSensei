from collections import Counter
from random import choice
from random import randint

_ex_boards = [
    [
        [0,0,3, 4,7,5, 1,2,9],
        [1,0,0, 3,0,2, 0,0,0],
        [0,2,0, 1,9,0, 0,8,0],

        [0,0,0, 6,0,7, 9,0,0],
        [0,1,8, 2,0,9, 6,7,0],
        [0,9,7, 5,1,8, 0,0,0],

        [7,0,6, 9,0,0, 0,0,0],
        [0,0,0, 7,2,1, 0,0,0],
        [2,0,1, 8,0,4, 7,9,0]
    ],
    [
        [7,8,0, 4,0,0, 1,2,0],
        [6,0,0, 0,7,5, 0,0,9],
        [0,0,0, 6,0,1, 0,7,8],

        [0,0,7, 0,4,0, 2,6,0],
        [0,0,1, 0,5,0, 9,3,0],
        [9,0,4, 0,6,0, 0,0,5],

        [0,7,0, 3,0,0, 0,1,2],
        [1,2,0, 0,0,7, 4,0,0],
        [0,4,9, 2,0,6, 0,0,7]
    ]
]

BLANK = 0
DIGITS = set(range(1,10))

def get_row(board, row):
    return set(board[row])

def is_valid(row):
    return Counter(row) == Counter(DIGITS)

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

def rotate_matrix_right(board):
    return [[board[j][i] for j in range(len(board))] for i in range(len(board[0])-1,-1,-1)]


def generate_board():
    m = choice(_ex_boards)
    for _ in range(randint(0, 3)):
        m = rotate_matrix_right(m)
    return m
