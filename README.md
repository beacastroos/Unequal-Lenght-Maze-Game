# Unequal Lenght Maze Game

Find a path from the bottom-left corner to the top-right corner, passing through each white square exactly once. The path must alternate between horizontal and vertical segments, and two consecutive segments cannot have the same length.

We provide Python scripts that create, give hints, and solve predefined levels of the game, as well as an option to create and solve your own maze.

Project for the Elements of Artificial Intelligence and Data Science course. 
Project grade: 20/20.

## Required Libraries:
### For the game:
- ```pip install -r requirements.txt ```

## How to Start the Game:

Open the folder containing the scripts and run the following command:

- ```python main.py ```

The game will launch automatically.

## How to Play:
### Instructions for Pre-Selected Levels:
- After opening the game, select a level.
- To play, you can move using the arrow keys or by clicking the desired square with the left mouse button.
- To request a hint, you can press the 'H' key on your keyboard or click the corresponding button.
- To let one of the algorithms solve the maze, click the respective button or press the keyboard shortcut indicated in parentheses next to the algorithm's name.
- If you win, a "You Won!" message will appear, and you will return to the main menu.
- If there is no solution or you have chosen an impossible path, an "Impossible Game!" message will appear, and you'll be redirected back to the main screen.

### Instructions for 'Build Your Own Maze':
- Select 'Build your own maze' from the main menu.
- Choose the dimensions of the maze by entering two numbers separated by a space, representing the number of rows and columns, then press Enter.
- Select where to place obstacles/walls by clicking the desired square with the left mouse button.
- To remove a wall, click the wall with the left mouse button.
- Once you have selected the desired walls, click 'Done' or press Enter.
- Play using the instructions given for pre-selected levels.
	
