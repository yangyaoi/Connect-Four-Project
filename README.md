# 4-to-Connect
4-to-Connect is a computer program created using python and Pygame. It is based on the classic game Connect 4.

# Game Description

# Game Controls
Users interact with the program with a mouse. Once 4-to-Connect is run, a user must press the start button in order to start game play. The first user to make a move will be player 1 and use red disks. The second user to make a move will use yellow disks and become player 2. When it is a players turn to make a move, they must click the unfilled column that they would like to drop a disk in. This unfilled column will be highlighted grey. The disk representing their colour will appear in the last empty slot of the column and the other player can then make a move.


# Installation

## System Requirement
* Windows10/MacOS Catalina/Linux Ubuntu
* Python 3.7.x
* Pygame1.9.2 or above

## How to install Python
1. Download Python 3.7.x from [here](https://www.python.org/downloads/release/python-375/)
2. Install Python by opening the downloaded file
3. For Windows user, please do not forget to set environment variable correctly

## How to install Pygame
1. If you have 'pip' installed, type the following command in terminal/command prompt
```
$ pip install pygame
```
2. Otherwise, please dowonload get-pip.py [here](https://bootstrap.pypa.io/get-pip.py) and type the following command in terminal/command prompt
```
$ python get-pip.py
```
   and go back to step 1

## Download our game
1. On this page, click "Clone or download" and then choose "Download ZIP"
2. Extract the zip file and open Codes folder
3. Double click the file named "ConnectFourGUI.py"

# Documentation
## Directory Structure
	
## Major Classes and Methods

Major classes of the code used to put together the game application include Main, ConnectFourGUI, ConnectFourBoard, Controller and Button. The Main class includes methods getBoard(), getGUI() and main(), where main() runs the application and connects any adjustments in ConnectFourBoard to the ConnectFourGUI. The ConnectFourGUI includes a few update methods to change the state of the GUI when the game is being played. These methods include updateColumnButtons(), update_screen(), help_view(), play_game(), exit_game(), game_over(), reset_board(), draw_board() and create_text(). The ConnectFourBoard class is used to simulate the gameplay using methods that represents rules in the game such as drop(), check_for_win(), switch_turn() and is_game_over(). There are also helper functions for the board to work, which include check_win_at_position(), alternation(), valid_move(), get_drop_loc(), whos_turn and other_player(). The Controller class acts as a helper class for the GUI, which includes a method called wait_click() that detects clicking events and sends the x and y coordinates to the GUI. The Button class is used as a sensor object for the GUI, where the user can click their mouse and activate a change in the state of the GUI. The Button includes place(), change_colour() and reset_colour() to indicate which player's piece is on that button.

# Code Extension

4-to-Connect does not allow users to view the start page from the play page. To allow this, one can add to the update_screen method so that buttons can beplaced on the screen if self.isPlaying is True.
## Change the colour of the board
If you want to change the colour of the board, you can check the draw board method in the ConnectFourGUI class. In the third "For" loop, there is a function "pygame.draw.rect", you can change the argument of the function to change the colour of the board.
## Change the colour of the stones
If you want to change the colour of disks, you can go into the class ConnectFourGui. There is a method "update screen". In the method, you should check into "elif self.isPlaying" statement, where there is a " if turn == P1" statement. Next, just change the argument of the function "pygame.draw.circle"
## Change the game rule
The game rule is in the default setting, which is connect four. However, one can change the game rule with the method "alternation" in the class "ConnectFourBoard". In the method, there is a statement "for i in range(4)". We can change the game into "Connect 3","Connect 5" , "connect 6" by changing the integer in the function "range".For example, if I want to play "connect 3", I can just simply change the statement to "for i in range(3)".

# Creators

# Individual Contributions

Hafsah Moalim:

I contributed to this project's code by creating the class skeleton for ConnectFourGUI and filling in some of its methods. In particular, I created the help page and start page for the game. In the init method for ConnectFourGUI, I used the Button class to  allow switching between the help and start page. I also made the create_text function  to make text appear on the screen. For the README file, I created section headers and  filled in some of the game controls and code extension sections.

* Gen Tomita
	* My main contribution on this project is to write the controller part of our MVC design in GUI class. Since I could not share a pygame object in multiple classes, I have integralated the ability of the controller class into GUI so that the model is updated simultaneously as GUI by user input. I have also debugged some functions in Board class and solved minor bugs such as the timing of increments. For README I wrote the instruction for how to download required dependencies and set up them properly.

Yao
For coding the game, I cooperated with team member Hafsah to finish the GUI class. In particular, I created the game over page, which will show when the game ends. I also created a predictor for dropping chess pieces and also an indicator for the user's mouse movement(It tells the user which column they are at and where is the chess pieces dropping spot in that column ). Moreover, I also created a button class to simplify the code. For readme, I completed the code extension part, especially in how to change the colour of the board, chess pieces and also how to change the game rule.
# Licence
