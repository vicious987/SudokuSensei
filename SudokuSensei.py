#!/usr/bin/env python3
import config as cfg
import pygame
import SudokuTools 

#TODO
#victory/losing screen
#interupt gui_solver

class SudokuGrid():

    def __init__(self, surf, matrix):
        self.surface = surf
        self.matrix = matrix
        self.width, self.height = surf.get_width() , surf.get_height()
        self.squares = [[Square(self.surface, i, j, matrix[i][j]) for j in range(9)] for i in range(9)]
        self.sqr_size = self.width / 9
        self.selected_sqr = None

    def draw(self):
        for i in range(1,10):
            thickness = cfg.LINE_SIZE_NORMAL if i % 3 != 0 else cfg.LINE_SIZE_THICK
            j = i * self.sqr_size
            pygame.draw.line(self.surface, cfg.LINE_COLOR, (0, j), (self.width, j), thickness)
            pygame.draw.line(self.surface, cfg.LINE_COLOR, (j, 0), (j, self.height), thickness)

        for row in self.squares:
            for sqr in row:
                sqr.draw()

    def deselect(self):
        if self.selected_sqr is None:
            return
        self.selected_sqr.highlighted = False
        self.selected_sqr = None
    
    def set_both(self, r, c, d):
        self.squares[r][c].set(d)
        self.matrix[r][c] = d

    def reset_board(self):
        for row in self.squares:
            for s in row:
                if not s.const:
                    self.set_both(s.row, s.col, 0)


    def solve_and_draw(self):
        r, c = SudokuTools.find_blank(self.matrix)
        if r is None:
            return True

        for d in SudokuTools.DIGITS: 
            if d in SudokuTools.get_viable_digits(self.matrix, r, c):
                self.set_both(r, c, d)
                self.squares[r][c].solver_draw(backtracked = False)
                pygame.display.update()
                pygame.time.delay(cfg.SOLVER_DELAY)
                if self.solve_and_draw():
                    return True

                self.set_both(r, c, 0)
                self.squares[r][c].solver_draw(backtracked = True)
                pygame.display.update()
                pygame.time.delay(cfg.SOLVER_DELAY)
        return False

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

        if self.squares[x][y].const:
            return False

        self.deselect()
        self.selected_sqr = self.squares[x][y]
        self.selected_sqr.highlighted = True
        return True


    def fill_selected_sqr(self, digit:str) -> bool:
        if self.selected_sqr is None:
            return False
        r, c = self.selected_sqr.row, self.selected_sqr.col
        self.set_both(r, c, int(digit))
        return True

    def is_victorious(self):
        if not self.is_finished():
            return False

        valid_rows = all([SudokuTools.is_valid(SudokuTools.get_row(self.matrix, i)) for i in range(9)])
        valid_cols = all([SudokuTools.is_valid(SudokuTools.get_col(self.matrix, i)) for i in range(9)])
        valid_boxes = all([SudokuTools.is_valid(SudokuTools.get_box(self.matrix, i, j)) for i in range(3) for j in range(3)])
        return valid_rows and valid_cols and valid_boxes 

    def is_finished(self): #replace with "to fill tracker"
        for i in range(9):
            for j in range(9):
                if self.squares[i][j].value == 0:
                    return False
        return True


class Square():
    def __init__(self, surf, row, col, val):
        self.row = row
        self.col = col 
        self.value = val
        self.const = val != 0 
        self.surface = surf
        self.highlighted = False

        self.size = surf.get_width() / 9 
        self.x = col * self.size 
        self.y = row * self.size
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

    
    def draw(self):
        font = pygame.font.SysFont(pygame.font.get_default_font(), cfg.DIGIT_FONT_SIZE)
        text_color = cfg.DIGIT_CONST_COLOR if self.const else cfg.DIGIT_MUTABLE_COLOR
        text = font.render(str(self.value), 1, text_color)
        dest = (self.x + (self.size/2 - text.get_width()/2), self.y + (self.size/2 - text.get_height()/2))
        self.surface.blit(text, dest)

        if self.highlighted:
            pygame.draw.rect(self.surface, cfg.HIGHLIGHT_COLOR, self.rect, 3)

    def solver_draw(self, backtracked):
        pygame.draw.rect(self.surface, cfg.BG_COLOR, self.rect, 0)
        self.draw()
        color = cfg.SOLVER_INP_BACKTRACK_COLOR if backtracked else cfg.SOLVER_INP_COLOR
        pygame.draw.rect(self.surface, color, self.rect, 3)

    def set(self, v):
        self.value = v

pygame.init()
window = pygame.display.set_mode(cfg.WINDOW_SIZE)
pygame.display.set_caption(cfg.WINDOW_NAME)
g = SudokuGrid(window, SudokuTools.generate_board())
is_running = True

while is_running:
    window.fill(cfg.BG_COLOR)
    g.draw()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            g.select_sqr(pygame.mouse.get_pos())

        if event.type == pygame.KEYDOWN:
            input = pygame.key.name(event.key)
            if input in "0123456789":
                g.fill_selected_sqr(input)
            if input == cfg.KEY_CHECK_VICTORY:
                if g.is_victorious():   #replace with some victory/losing screen
                    print("yay! :)")
                else:
                    print("nay! :(")
            if input == cfg.KEY_RUN_SOLVER:
                g.deselect()
                g.reset_board()
                g.solve_and_draw()
            if input == cfg.KEY_RESTART_BOARD:
                g.reset_board()

        if event.type == pygame.QUIT:
            is_running = False

    pygame.display.update()
