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
