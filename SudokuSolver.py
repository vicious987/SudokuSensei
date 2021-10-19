#!/usr/bin/env python3
import SudokuToolset

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

#tools.printboard(t)
SudokuToolset.printboard(t)
SudokuToolset.fill(t)
print("---------------------------------------")
SudokuToolset.printboard(t)
