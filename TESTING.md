# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.

## Code Validation

I manually tested all inputs and functions to make sure that the game operates as intended.  This included:

- The Intro Screen Functionality:
![screenshot](documentation/testing/intro_screen.png)

Here the user has three options.  Entering '1' will give the user a look at the full instructions for the game.
![screenshot](documentation/testing/intro_instructions.png)
![screenshot](documentation/testing/instructions.png)

Entering '2' will allow the user to play the game.
![screenshot](documentation/testing/intro_play_game.png)
![screenshot](documentation/testing/intro_play_game_open.png)

Entering '3' will allow the user to quit the game. 
![screenshot](documentation/testing/intro_quit_game01.png)
![screenshot](documentation/testing/intro_quit_game02.png)

Entering anything other than '1', '2', or '3' will give the user an invalid input message.
![screenshot](documentation/testing/intro_wrong_input01.png)
![screenshot](documentation/testing/intro_wrong_input02.png)

- Playing the Game

When the game opens, the Player is prompted to go first by entering a valid row and column.
![screenshot](documentation/testing/intro_play_game_open.png)

Entering anything other than '0', '1', '2', or '3' will result in an invalid input message.
![screenshot](documentation/testing/play_game_invalid_row01.png)
![screenshot](documentation/testing/play_game_invalid_col01.png)
![screenshot](documentation/testing/play_game_invalid_row02.png)

After the Player makes a valid move, the board is updated and the player can see the move they just made.
![screenshot](documentation/testing/play_game_valid_input01.png)
![screenshot](documentation/testing/play_game_valid_input02.png)

When it is time for the Computer to make its move, a message appears to let the Player know that the Computer is moving, followed by printing the board to show the Player where the Computer has moved.
![screenshot](documentation/testing/play_game_comp_move01.png)
![screenshot](documentation/testing/play_game_comp_move02.png)

This continues until the game is finished.

During the game, attempting to place a piece on a space that is already occupied will result in an invalid input message.
![screenshot](documentation/testing/play_game_invalid_move01.png)
![screenshot](documentation/testing/play_game_invalid_move02.png)
![screenshot](documentation/testing/play_game_invalid_move03.png)
![screenshot](documentation/testing/play_game_invalid_move04.png)

There is an accurate score tracker which the Player may refer to throughout the course of the game to keep an eye on the score tally.
![screenshot](documentation/testing/play_game_score_tracker01.png)
![screenshot](documentation/testing/play_game_score_tracker02.png)

When all spaces on the board are occupied, the game is over.  At this point, the final score is revealed, and a winner is declared.  The user is also given the option to enter 'Y' to start a new game, or 'N' to quit the program.
![screenshot](documentation/testing/end_game01.png)

Entering anything other than 'Y' or 'N' gives an invalid input message.
![screenshot](documentation/testing/end_game02.png)
![screenshot](documentation/testing/end_game03.png)

Entering 'N' quits the game.
![screenshot](documentation/testing/end_game04.png)
![screenshot](documentation/testing/end_game05.png)

Entering 'Y' starts a new game.
![screenshot](documentation/testing/end_game06.png)
![screenshot](documentation/testing/end_game07.png)

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

