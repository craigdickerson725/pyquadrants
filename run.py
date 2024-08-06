import random # This is for the computer ai
from colorama import Fore, Back, Style, init # This is for coloring quadrants
"""
The os and sys imports are for the 'any key' input at the end of the game
"""
import os
import sys

"""
Initializes colorama to color the quadrants
"""
init()

"""
This class will define the game's methods and attributes
"""
class PyQuadrants:
    def __init__(self):
        self.reset_game()
        self.colors = {
            'quadrant_1': Back.RED,
            'quadrant_2': Back.GREEN,
            'quadrant_3': Back.YELLOW,
            'quadrant_4': Back.BLUE,
            'endc': Style.RESET_ALL
        }

    """
    This is to initialize/reset the game board, player info, and territories
    """
    def reset_game(self):
        self.board = [['.' for _ in range(4)] for _ in range(4)]
        self.players = ['Player', 'Computer']
        self.pieces = ['X', 'Y']  # X for Player, Y for Computer
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

    """
    This is to make sure a move is valid
    """
    def is_valid_move(self, row, col):
        return self.board[row][col] == '.'

    """
    This places a piece on the board and updates the territories
    """
    def place_piece(self, row, col, piece):
        if self.is_valid_move(row, col):
            self.board[row][col] = piece
            self.update_territories(row, col, piece)
            return True
        return False

    def update_territories(self, row, col, piece):
        current_player = self.players[self.current_player_index]
        
        # Checks the row
        self.territories[current_player] += self.score_territory([self.board[row][i] for i in range(4)], piece)
        
        # Checks the column
        self.territories[current_player] += self.score_territory([self.board[i][col] for i in range(4)], piece)
        
        # Checks the quadrant
        start_row, start_col = 2 * (row // 2), 2 * (col // 2)
        self.territories[current_player] += self.score_territory([self.board[i][j] for i in range(start_row, start_row + 2) for j in range(start_col, start_col + 2)], piece)

    """
    This checks how many points to give
    """
    def score_territory(self, lst, piece):
        if lst.count(piece) == 4:
            return 2
        elif lst.count(piece) == 3:
            return 1
        return 0

    """
    This asks for player to input move, and validates the move
    """
    def player_move(self):
        while True:
            try:
                row = int(input("Enter row (0-3): "))
                col = int(input("Enter col (0-3): "))
                if 0 <= row <= 3 and 0 <= col <= 3:
                    if self.place_piece(row, col, 'X'):
                        break
                    else:
                        print("Invalid move! Try again.")
                else:
                    print("Invalid input! Please enter a number between 0 and 3.")
            except ValueError:
                print("Invalid input! Enter numbers for row and col.")

    """
    This is to create ai for the computer's move.
    It will help the computer to pick an effective move.
    """
    def ai_move(self):
        best_move = None
        max_gain = -1
        
        for row in range(4):
            for col in range(4):
                if self.is_valid_move(row, col):
                    potential_gain = self.potential_gain(row, col, 'Y')
                    if potential_gain > max_gain:
                        max_gain = potential_gain
                        best_move = (row, col)
        
        if best_move:
            row, col = best_move
            self.place_piece(row, col, 'Y')
            print(f"Computer placed Y at ({row}, {col})")
    
    def potential_gain(self, row, col, piece):
        gain = 0

        # Checks gain potential in a row
        gain += self.score_territory([self.board[row][i] for i in range(4)], piece)

        # Checks gain potential in a column
        gain += self.score_territory([self.board[i][col] for i in range(4)], piece)

        # Checks gain potential in a quadrant
        start_row, start_col = 2 * (row // 2), 2 * (col // 2)
        gain += self.score_territory([self.board[i][j] for i in range(start_row, start_row + 2) for j in range(start_col, start_col + 2)], piece)

        return gain

    """
    This is the main game loop
    It switches between players and checks for the end of the game
    """
    def play_game(self):
        print("Welcome to PyQuadrants!")
        print("Player is 'X' and Computer is 'Y'.")
        print("Take turns to place your piece on the board.")
        print("Control more territories (rows, columns, or quadrants) to win.\n")

        while True:
            self.print_board()
            current_player = self.players[self.current_player_index]
            print(f"Territories - Player: {self.territories['Player']}, Computer: {self.territories['Computer']}")
            
            if current_player == "Player":
                print("Player's turn")
                self.player_move()
            else:
                print("Computer's turn")
                self.ai_move()

            self.current_player_index = (self.current_player_index + 1) % 2

            if all(self.board[row][col] != '.' for row in range(4) for col in range(4)):
                self.print_board()
                player_territories = self.territories['Player']
                computer_territories = self.territories['Computer']
                print(f"Final Score - Player: {player_territories}, Computer: {computer_territories}")
                if player_territories > computer_territories:
                    print("Player wins!")
                elif computer_territories > player_territories:
                    print("Computer wins!")
                else:
                    print("It's a draw!")
                break

        self.end_game()

    """
    This is for the end of the game
    It waits for the player to press a key to start a new game
    """
    def end_game(self):
        print("Click any key to begin a new game.")
        self.wait_for_key()
        self.reset_game()
        self.play_game()

    def wait_for_key(self):
        if os.name == 'nt':  # For Windows
            import msvcrt
            msvcrt.getch()
        else:  # For Unix-based systems (Linux, macOS)
            import termios, tty
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

"""
This initializes and starts the game
"""
if __name__ == "__main__":
    game = PyQuadrants()
    game.play_game()