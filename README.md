# [PYQUADRANTS](https://pyquadrants-ece1d63f094e.herokuapp.com)

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/craigdickerson725/pyquadrants)](https://github.com/craigdickerson725/pyquadrants/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/craigdickerson725/pyquadrants)](https://github.com/craigdickerson725/pyquadrants/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/craigdickerson725/pyquadrants)](https://github.com/craigdickerson725/pyquadrants)

Welcome to PyQuadrants!  This game is intended to run in the Code Institute mock terminal in Heroku.  As far as I know, I invented this game (though it started out based off of the Gigamic game 'Quantik' and morphed into something totally different).  In this game, players will compete against the computer to gain control over rows, columns, or quadrants.  My idea was to create a game that required strategy, but which is easy to understand by adults and children alike.  Also, the game only takes a few minutes to play, so it is more likely to hold the user's interest until the end (unlike many strategy games).  The instructions are as follows:

### PyQuadrants Instructions

Instructions:

-The game board has four rows, four columns, and four quadrants.

-Rows are the horizontal lines, numbered from left to right.  

-Columns are the vertical lines, numbered from top to bottom.

-Quadrants are the four colored regions.

-The Player's game piece is X, and the Computer's is Y.

-Players take turns placing their respective game pieces on the board.

-The goal is to gain control of as many rows, columns, and quadrants as possible.

-Control is established when a player's game pieces fill at least three of the four available spaces on a row, column, or quadrant.

-Players continue taking turns placing their respective game pieces on the board until there are no more available spaces.

-When there are no more available spaces remaining on the game board, then the game is over, and the player with the most points wins.

Scoring:

-Control is when three of four available spaces on a row, column, or quadrant are represented by one player.  
Control = 1 point

-Complete Control is when all four available spaces of a row, column, or quadrant are represented by one player.
Complete Control = 3 points

Good Luck!

![screenshot](documentation/mockup.png)

source: [amiresponsive](https://ui.dev/amiresponsive?url=https://pyquadrants-ece1d63f094e.herokuapp.com)

## UX

Being a big fan of both board games and strategy games, I thought I'd tackle creating one myself.  One of the goals was to keep it simple, short, and sweet, so I decided upon a square board with sixteen spaces.  The four spaces in each of the corners (quadrants) are colored, to show that they are each regions of their own.  So altogether, we have:  four rows, four columns, and four quadrants. The user and computer trade turns putting down their respective game pieces until the board is full.

## Features

### Existing Features

- **Colored Game Board**

    - The game board features colors and a clearly marked grid to ensure that the user has a clear understanding of the available moves and territories.

![screenshot](documentation/features/feature01.png)

- **Easy to Use Input for Player Moves**

    - The inputs for recording the Player's moves are clear and easy to use.  Simply add the row number and press ENTER, then the column number and press ENTER.  Easy-peasy!

![screenshot](documentation/features/feature02.png)

- **Clear Indicator to Show Each Computer Move**

    - After each move by the Computer, the Player can see clearly where the Computer placed its piece.  It is both visible on the game board and written above the board.

![screenshot](documentation/features/feature03.png)

- **Active Score Tracker**

    - There is a score tracker, which the player may refer to at any time to see how many points each participant currently has.

![screenshot](documentation/features/feature04.png)

- **End of Game Message With Option to Play Again or Exit**

    - When the game is over, there is a message announcing the winner (or a draw, when applicable), with an option to press Y to start a new game, or to press N to exit the game.

![screenshot](documentation/features/feature05.png)

- **Invalid Input Messages**

    - When the Player enters an invalid choice, an Invalid Input Error is given.  This also happens when the Player attempts to place a piece on an already occupied space.

![screenshot](documentation/features/feature06.png)

![screenshot](documentation/features/feature07.png)

- **Option to View Instructions, Play or Exit Game**

    - Upon starting the program, the Player is given an option to view the complete instructions, so that they may understand how to play the game.  Alternately, the Player may choose the option to Play, or Exit the game.

![screenshot](documentation/features/feature08.png)

![screenshot](documentation/features/feature09.png)

![screenshot](documentation/features/feature10.png)

![screenshot](documentation/features/feature11.png)