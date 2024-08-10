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

### Future Features

- Player Option to Increase Game Board Size
    - For strategy gamers who have that kind of time on their hands, it would be great to add a 'medium' sized board, which would be four times larger than the normal size.  A 'big' sized board would be sixteen times the normal size--which would be for those extreme gamers!
- Multi-player Capability
    - It would be great to allow friends to play against one another, instead of against the computer.

## Tools & Technologies Used

- [![Markdown Builder](https://img.shields.io/badge/Markdown_Builder-grey?logo=markdown&logoColor=000000)](https://tim.2bn.dev/markdown-builder) used to generate README and TESTING templates.
- [![Git](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [![GitHub](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) used for secure online code storage.
- [![Gitpod](https://img.shields.io/badge/Gitpod-grey?logo=gitpod&logoColor=FFAE33)](https://gitpod.io) used as a cloud-based IDE for development.
- [![Python](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) used as the back-end programming language.
- [![Heroku](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) used for hosting the deployed back-end site.
- [![ChatGPT](https://img.shields.io/badge/ChatGPT-grey?logo=chromatic&logoColor=75A99C)](https://chat.openai.com) used to help debug, troubleshoot, and explain things.

## Data Model

### Classes & Functions

The program uses classes as a blueprint for the project's objects (OOP). This allows for the object to be reusable.

```python
class PyQuadrants:
    """ This class defines the game's methods and attributes """
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
```

The primary functions used on this application are:

- `__init__(self)`
    - Initializes the game by resetting the board, setting up player information, and defining the colors for each quadrant.
- `reset_game(self)`
    - Resets the game board, player info, and territory scores, preparing the game for a new session.
- `print_board(self)`
    - Prints the current state of the game board, with each quadrant colored according to its position.
- `color_cell(self, row, col, cell)`
    - Colors a specific cell on the board based on its quadrant.
- `is_valid_move(self, row, col)`
    - Checks if a move is valid by ensuring the selected cell is empty.
- `place_piece(self, row, col, piece)`
    -  Places a player's piece on the board and updates the territory scores if the move is valid.
- `update_territories(self, row, col, piece)`
    -  Updates the territory score for the current player based on the latest move, checking rows, columns, and quadrants.
- `score_territory(self, lst, piece)`
    -  Calculates and returns the score for a given row, column, or quadrant based on how many pieces are controlled by the player.
- `player_move(self)`
    -  Handles input from the player for making a move, validating the input and the move.
- `ai_move(self)`
    -  Manages the computer's move by selecting the most effective move based on potential score gain.
- `potential_gain(self, row, col, piece)`
    -  Calculates the potential score gain for a specific move, used by the AI to decide its move.
- `intro(self)`
    -  Displays the introduction screen with options to view instructions, start the game, or quit.
- `instructions(self)`
    -  Provides detailed instructions on how to play the game.
- `play_game(self)`
    -  The main game loop that alternates turns between the player and the computer, checking for the end of the game after each move.
- `end_game(self)`
    -  Manages the end of the game, offering the player a choice to start a new game or exit.
- `clear()`
    -  Clears the terminal screen, keeping the output clean and easy to read.

### Imports

I've used the following Python packages and/or external imported packages.
- `os`: used for adding a `clear()` function
- `colorama`: used for including color in the terminal
- `random`: used to get a random choice from a list
- `time`: used to give space between player's move and computer's move

## Testing

> [!NOTE]  
> For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

Code Institute has provided a [template](https://github.com/Code-Institute-Org/python-essentials-template) to display the terminal view of this backend application in a modern web browser.
This is to improve the accessibility of the project to others.

The live deployed application can be found deployed on [Heroku](https://pyquadrants-ece1d63f094e.herokuapp.com).

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set the value of KEY to `PORT`, and the value to `8000` then select *add*.
- If using any confidential credentials, such as CREDS.JSON, then these should be pasted in the Config Variables as well.
- Further down, to support dependencies, select **Add Buildpack**.
- The order of the buildpacks is important, select `Python` first, then `Node.js` second. (if they are not in this order, you can drag them to rearrange them)

Heroku needs three additional files in order to deploy properly.

- requirements.txt
- Procfile
- runtime.txt

You can install this project's **requirements** (where applicable) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:

- `echo web: node index.js > Procfile`

The **runtime.txt** file needs to know which Python version you're using:
1. type: `python3 --version` in the terminal.
2. in the **runtime.txt** file, add your Python version:
	- `python-3.9.19`

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The frontend terminal should now be connected and deployed to Heroku!

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.

- `pip3 install -r requirements.txt`.

If using any confidential credentials, such as `CREDS.json` or `env.py` data, these will need to be manually added to your own newly created project as well.

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/craigdickerson725/pyquadrants) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	- `git clone https://github.com/craigdickerson725/pyquadrants.git`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/craigdickerson725/pyquadrants)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/craigdickerson725/pyquadrants)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Local VS Deployment

To my knowledge (as pertaining to testing in both the local and deployed versions of the program), there are no differences between the local version and deployed version.

### Content

| Source | Location | Notes |
| --- | --- | --- |
| [Markdown Builder](https://tim.2bn.dev/markdown-builder) | README and TESTING | tool to help generate the Markdown files |
| [StackOverflow](https://stackoverflow.com/a/2450976) | quiz page | Fisher-Yates/Knuth shuffle in JS |
| [Geeks for Geeks](https://www.geeksforgeeks.org/clear-screen-python/) | python basics | how to clear screen in python |
| [Stack Overflow](https://stackoverflow.com/questions/2084508/clear-the-terminal-in-python) | questions | clear the terminal in python |
| [YouTube](https://www.youtube.com/watch?v=u51Zjlnui4Y) | PP3 terminal | tutorial for adding color to the Python terminal |

### Acknowledgements

- I would like to thank my Code Institute mentor, [Tim Nelson](https://github.com/TravelTimN) for his support throughout the development of this project.
- I would like to thank the [Code Institute Slack community](https://code-institute-room.slack.com) for the moral support; it kept me going during periods of self doubt and imposter syndrome.
- I would like to thank my wife (Julia) and my daughter (Serafina) for their patience in playing this game many, many times; their testing and critiques helped me to stay on track.
- I would like to thank my aunt (Sarah) for her input as I worked out the game rules.
