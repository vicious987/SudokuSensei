"""configuration file for sudoku_sensei"""
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
BLUE = (0, 0, 255)

# window settings
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
WINDOW_NAME = "SudokuSensei"

# board colors and sizes
DIGIT_FONT_SIZE = 40
DIGIT_CONST_COLOR = BLACK   # non-changeable digits
DIGIT_MUTABLE_COLOR = GRAY  # digits changeable by player
BG_COLOR = WHITE            # board background color
HIGHLIGHT_COLOR = BLUE      # color of square chosen by player

# sudoku board seperator
LINE_COLOR = BLACK
LINE_SIZE_NORMAL = 1
LINE_SIZE_THICK = 4

# solver configs
SOLVER_INP_COLOR = GREEN            # highlight color of filled squares
SOLVER_INP_BACKTRACK_COLOR = RED    # highlight color of backtracked squares
SOLVER_DELAY = 50            #defines delay in ms between solver inputs

# key bindings
KEY_RUN_SOLVER = "space"
KEY_RESTART_BOARD = "r"
KEY_CHECK_VICTORY = "return"
