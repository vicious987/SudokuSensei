#!/usr/bin/env python3
import SudokuToolset
import pygame

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
"""
board = [
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
"""
t = t1 

BLACK = (0,0,0)
WHITE = (255, 255, 255)

class SudokuGrid():

    def __init__(self, surf):
        self.surface = surf
        self.width, self.height = surf.get_width() , surf.get_height()
        self.squares = [[Box(self.surface, i, j, t[i][j]) for j in range(9)] for i in range(9)]

    #def update(self):
    #    self.model = [[self.squares[i][j].value for j in range(9)] for i in range(9)]

    def draw(self):
        sqr_size = self.width / 9
        for i in range(9+1):
            thickness = 4 if (i % 3 == 0 and i != 0) else 1
            pygame.draw.line(self.surface, BLACK, (0, i * sqr_size), (self.width, i * sqr_size), thickness)
            pygame.draw.line(self.surface, BLACK, (i * sqr_size, 0), (i * sqr_size, self.height), thickness)

        for row in self.squares:
            for sqr in row:
                sqr.draw()

class Box():
    def __init__(self, surf, row, col, val, const=True):
        self.row = row
        self.col = col 
        self.value = val
        self.const = const
        self.surface = surf

        self.size = surf.get_width() / 9
        self.x = col * self.size 
        self.y = row * self.size 
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

    
    def draw(self):
        font = pygame.font.SysFont(pygame.font.get_default_font(), 40)
        text = font.render(str(self.value), 1, (0,0,0))
        dest = (self.x + (self.size/2 - text.get_width()/2), self.y + (self.size/2 - text.get_height()/2))
        self.surface.blit(text, dest)

    def set_value(self, v):
        self.value = v

pygame.init()
window = pygame.display.set_mode(size=(800, 800))
pygame.display.set_caption("SudokuSensei")
g = SudokuGrid(window)
is_running = True

while is_running:
    window.fill(WHITE)
    g.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
    pygame.display.update()
