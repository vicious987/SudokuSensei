#!/usr/bin/env python3

x = '_'
t1 = [
#    0 1 2  3 4 5  6 7 8 
    [x,x,3, 4,7,5, 1,2,9], #0
    [1,x,x, 3,x,2, x,x,x], #1
    [x,2,x, 1,9,x, x,8,x], #2

    [x,x,x, 6,x,7, 9,x,x], #3
    [x,1,8, 2,x,9, 6,7,x], #4
    [x,9,7, 5,1,8, x,x,x], #5

    [7,x,6, 9,x,x, x,x,x], #6
    [x,x,x, 7,2,1, x,x,x], #7
    [2,x,1, 8,x,4, 7,9,x], #8
]

t = t1 

class toolset:
    blank = 0
    digits = set(range(1,10))

    @staticmethod
    def get_row(board, row):
        return set(board[row])


    @staticmethod
    def get_col(board, col):
        return set([board[row][col] for row in range(9)])

    @staticmethod
    def get_box(board, row, col):
        i, j= row // 3, col // 3
        sqr = [row[j*3:j*3+3] for row in board[i*3:i*3+3]] #sqr as list of rows
        return set([x for sub in sqr for x in sub]) #flattening

    @staticmethod
    def get_viable_vertical(board, row) -> set:
        return toolset.digits - toolset.get_row(board, row)

    @staticmethod
    def get_viable_horizontal(board, col) -> set:
        return toolset.digits - toolset.get_col(board, col)

    @staticmethod
    def get_viable_box(board, row, col) -> set:
        return toolset.digits - toolset.get_box(board, row, col)
    @staticmethod
    def get_viable_digits(board, row, col) -> set:
        return toolset.viable_vertical(board, row) & toolset.viable_horizontal(board, row) & toolset.viable_box(board, row, col)

    @staticmethod
    def find_blank(board):
        for i in range(9):
            for j in range(9):
                return i, j if board[i][j] == toolset.blank else None, None

    @staticmethod
    def fill(board):
        x, y = toolset.find_blank(board)
        if x is None:
            return True

        for d in toolset.get_viable_digits(board, x, y):
            board[x][y] = d
            if toolset.fill(board):
                return True
            board[x][y] = toolset.blank

        return False









