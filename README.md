# What is it?
SudokuSensei is a playable sudoku puzzle and backtracking visualisation tool. 

It generates a sudoku board that You can solve. It can also solve itself, visualising each step along the way.

![input gif](https://imgur.com/kzOCrHY)

# How do I install it?
## Dependencies
    python3
    pygame
## Linux based OS 
### Ubuntu
First, make sure you have python3 installed with:

    sudo apt update
    sudo apt install python3

Python packages such as pygame are easy to install with pip. pip is shipped automatically with python3.4+, but you can make sure it's installed with:

    sudo apt update
    sudo apt install python3-pip 

And finally, install pygame package:

    pip install pygame

### Windows (Not tested)
1. Download and install Python3 from https://www.python.org/downloads/release/python-3100/ 
2. Install pygame by following instructions on https://www.pygame.org/wiki/GettingStarted 
3. Clone / Download this repository


# How do I run it? 
## Linux based OS 
### Ubuntu
Move to project folder and run with python:

    python3 SudokuSensei.py

Or make it executable and run as script:

    sudo chmod +x SudokuSensei.py
    ./SudokuSensei.py
## Windows (Not tested)
1. move to directory via terminal
2. py REPLACE_WITH_PROJECT_PATH\SudokuSensei.py

Or
1. move to with explorer
2. right click on SudokuSensei.py
3. open with python 

    

# How do I use it?

* **left mouse button** to select a square, then use keyboard to fill in a square with your guess
* **space** to use solver
* **enter** to check if sudoku is solved properly
* **r** to restart
* **esc** to quit

![Solver gif](https://imgur.com/kzOCrHY)
# How do I configure it?
Sudoku board is customizable with config.py script.

You can change colors, windows size, font size, line thickness, etc and rebind keys by playing around with values.

Speed (delay between moves) at which solver fills the board is customizable as well.
