#!/usr/bin/env python3

t1 = [
#    0 1 2  3 4 5  6 7 8 
    [0,0,3, 4,7,5, 1,2,9], #0
    [1,0,0, 3,0,2, 0,0,0], #1
    [0,2,0, 1,9,0, 0,8,0], #2

    [0,0,0, 6,0,7, 9,0,0], #3
    [0,1,8, 2,0,9, 6,7,0], #4
    [0,9,7, 5,1,8, 0,0,0], #5

    [7,0,6, 9,0,0, 0,0,0], #6
    [0,0,0, 7,2,1, 0,0,0], #7
    [2,0,1, 8,0,4, 7,9,0], #8
]

t = t1 

class SudokuToolset:
    BLANK = 0
    DIGITS = set(range(1,10))

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
        return SudokuToolset.DIGITS - SudokuToolset.get_row(board, row)

    @staticmethod
    def get_viable_horizontal(board, col) -> set:
        return SudokuToolset.DIGITS - SudokuToolset.get_col(board, col)

    @staticmethod
    def get_viable_box(board, row, col) -> set:
        return SudokuToolset.DIGITS - SudokuToolset.get_box(board, row, col)
    @staticmethod
    def get_viable_digits(board, row, col) -> set:
        return SudokuToolset.get_viable_vertical(board, row) & SudokuToolset.get_viable_horizontal(board, col) & SudokuToolset.get_viable_box(board, row, col)

    @staticmethod
    def find_blank(board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == SudokuToolset.BLANK:
                    return i, j
        return None, None
                #return (i, j) if board[i][j] == SudokuToolset.BLANK else (None, None)

    @staticmethod
    def fill(board):
        x, y = SudokuToolset.find_blank(board)
        if x is None:
            return True
        
        for d in SudokuToolset.DIGITS:
            if d in SudokuToolset.get_viable_digits(board, x, y):
                board[x][y] = d
                if SudokuToolset.fill(board):
                    return True
                board[x][y] = SudokuToolset.BLANK
        return False

    @staticmethod
    def printboard(board):
        for row in board:
            for i in row:
                print(i, end =" ")
            print()

SudokuToolset.printboard(t)
SudokuToolset.fill(t)
print("---------------------------------------")
SudokuToolset.printboard(t)
