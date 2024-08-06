import random
from colorama import Fore, Back, Style, init
import os
import sys

"""
To initialize colorama, which is needed to color the quadrants
"""
init()

"""
This class will define the game's methods and attributes
"""
class PyQuadrants:
    def __init__(self):
        self.reset_game()
        self.colors = {
            'quadrant1': Back.RED,
            'quadrant2': Back.GREEN,
            'quadrant3': Back.YELLOW,
            'quadrant4': Back.BLUE,
            'endc': Style.RESET_ALL
        }

    """
    This is to initialize/reset the game board, player info, and territories
    """
    def reset_game(self):
        self.board = [['.' for _ in range(4) for _ in range(4)]]
        self.players = ['Player', 'Computer']
        self.pieces = ['X', 'Y'] # X is for the player, Y is for the computer
        self.current_player_index = 0
        self.territories = {'Player': 0, 'Computer': 0}

    """
    Prints the current game board and sets the colors
    """
    def print_board(self):
        print("  0 1 2 3")
        for idx, row in enumerate(self.board):
            row_str = f"{idx} "
            for col, cell in enumerate(row):
                row_str += self.color_cell(idx, col, cell) + " "
            print(row_str + self.colors['endc'])
        print()

    def color_cell(self, row, col, cell):
        if row < 2 and col < 2:
            return self.colors['quadrant_1'] + cell
        elif row < 2 and col >= 2:
            return self.colors['quadrant_2'] + cell
        elif row >= 2 and col < 2:
            return self.colors['quadrant_3'] + cell
        else:
            return self.colors['quadrant_4'] + cell