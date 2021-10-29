"""
This module provides sudoku solving, validation, and generation tools.
"""

from collections import Counter
from random import choice
from random import randint

_EX_BOARDS = [
    [
        [0, 0, 3, 3, 7, 5, 1, 2, 9],
        [1, 0, 0, 3, 0, 2, 0, 0, 0],
        [0, 2, 0, 1, 9, 0, 0, 8, 0],
        [0, 0, 0, 6, 0, 7, 9, 0, 0],
        [0, 1, 8, 2, 0, 9, 6, 7, 0],
        [0, 9, 7, 5, 1, 8, 0, 0, 0],
        [7, 0, 6, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 2, 1, 0, 0, 0],
        [2, 0, 1, 8, 0, 4, 7, 9, 0]
    ],
    [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]
]

BLANK = 0
DIGITS = set(range(1, 10))

def is_valid(lst) -> bool:
    """checks given list if it's a valid sudoku set"""
    return Counter(lst) == Counter(DIGITS)

def get_row(board, row: int) -> set:
    """a helper function to select a row from sudoku board"""
    return set(board[row])

def get_col(board, col: int) -> set:
    """a helper function to select a row from sudoku board"""
    return set([board[row][col] for row in range(9)])

def get_box(board, row: int, col: int) -> set:
    """given cordinates, returns set of digits from sudoku 3x3 box"""
    i, j = row // 3, col // 3
    sqr = [row[j*3:j*3+3] for row in board[i*3:i*3+3]]  #sqr as list of rows
    return {x for sub in sqr for x in sub}              #flattening

def get_viable_vertical(board, row: int) -> set:
    """given cordinates, returns set of digits that are yet to be used in that vertical row"""
    return DIGITS - get_row(board, row)

def get_viable_horizontal(board, col: int) -> set:
    """given cordinates, returns set of digits that are yet to be used in that horizontal column"""
    return DIGITS - get_col(board, col)

def get_viable_box(board, row: int, col: int) -> set:
    """given cordinates, returns set of digits that are yet to be used in that box"""
    return DIGITS - get_box(board, row, col)

def get_viable_digits(board, row: int, col: int) -> set:
    """
    given cordinates of a square, returns digit set that is a viable fill option for that square
    """
    return (get_viable_vertical(board, row)
            & get_viable_horizontal(board, col)
            & get_viable_box(board, row, col))

def find_blank(board) -> (int, int):
    """finds first blank square in sudoku board"""
    for i in range(9):
        for j in range(9):
            if board[i][j] == BLANK:
                return i, j
    return None, None

def fill(board):
    """solves a sudoku with backtracking method"""
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
    """prints a sudoku board in terminal"""
    for row in board:
        for i in row:
            print(i, end=" ")
        print()

def rotate_matrix_right(board):
    """rotates matrix by 90. a helper function for generating sudoku boards"""
    return [[board[j][i] for j in range(len(board))] for i in range(len(board[0])-1, -1, -1)]

def generate_board():
    """
    creates a playable board.
    as of now, it's a dummy method
    """
    m = choice(_EX_BOARDS)
    for _ in range(randint(0, 3)):
        m = rotate_matrix_right(m)
    return m
