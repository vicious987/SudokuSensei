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

BG_COLOR = WHITE = (255, 255, 255)
FOCUS_COLOR = RED = (255,0,0)
GAME_DIGIT = BLACK = (0,0,0)
PLAYER_DIGIT = GRAY = (150,150,150)

class SudokuGrid():

    def __init__(self, surf):
        self.surface = surf
        self.width, self.height = surf.get_width() , surf.get_height()
        self.squares = [[Box(self.surface, i, j, t[i][j]) for j in range(9)] for i in range(9)]
        self.sqr_size = self.width / 9
        self.selected_sqr = None

    def draw(self):
        for i in range(1,10):
            thickness = 1 if i % 3 != 0 else 4
            j = i * self.sqr_size
            pygame.draw.line(self.surface, BLACK, (0, j), (self.width, j), thickness)
            pygame.draw.line(self.surface, BLACK, (j, 0), (j, self.height), thickness)

        for row in self.squares:
            for sqr in row:
                sqr.draw()

    def mousepos_to_gridpos(self, mouse_pos):
        mouse_y, mouse_x = mouse_pos
        if mouse_x < self.width and mouse_y < self.height:
            grid_x = int(mouse_x // self.sqr_size)
            grid_y = int(mouse_y // self.sqr_size)
            return grid_x, grid_y
        return None, None 

    def select_sqr(self, mouse_pos) -> bool:
        x, y = self.mousepos_to_gridpos(mouse_pos)
        if x is None:
            return False

        if self.selected_sqr is not None:
            self.selected_sqr.focus = False
        self.selected_sqr = self.squares[x][y]
        self.selected_sqr.focus = True
        return True

    def fill_sqr(self, digit:str) -> bool:
        if self.selected_sqr is None:
            return False
        return self.selected_sqr.enter_value(int(digit))


class Box():
    def __init__(self, surf, row, col, val, focus = False):
        self.row = row
        self.col = col 
        self.value = val
        self.const = val != 0 
        self.surface = surf
        self.focus = focus

        self.size = surf.get_width() / 9
        self.x = col * self.size 
        self.y = row * self.size 
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

    
    def draw(self):
        font = pygame.font.SysFont(pygame.font.get_default_font(), 40)
        text_color = GAME_DIGIT if self.const else PLAYER_DIGIT
        text = font.render(str(self.value), 1, text_color)
        dest = (self.x + (self.size/2 - text.get_width()/2), self.y + (self.size/2 - text.get_height()/2))
        self.surface.blit(text, dest)

        if self.focus:
            pygame.draw.rect(self.surface, FOCUS_COLOR, self.rect, 3)

    def set_value(self, v) -> bool:
        if not self.const:
            self.value = v
            return True
        return False

    def enter_value(self, v) -> bool:
        if self.focus:
            is_set = self.set_value(v)
            return is_set
        return False

pygame.init()
window = pygame.display.set_mode(size=(800, 800))
pygame.display.set_caption("SudokuSensei")
g = SudokuGrid(window)
is_running = True

while is_running:
    window.fill(BG_COLOR)
    g.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
            g.select_sqr(pygame.mouse.get_pos())
        if event.type == pygame.KEYDOWN:
            #print(event.key, event.mod, event.unicode, event.scancode)
            #print(pygame.key.name(event.key))
            input = pygame.key.name(event.key)
            if input in "0123456789":
                g.fill_sqr(input)

    pygame.display.update()
