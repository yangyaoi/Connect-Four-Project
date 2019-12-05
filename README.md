# 4-to-Connect
4-to-Connect is a computer program created using python and Pygame. It is based on the classic game Connect 4.

# Game Description

# Game Controls
Users interact with the program with a mouse. Once 4-to-Connect is run, a user must press the start button in order to start game play. The first user to make a move will be player 1 and use red disks. The second user to make a move will use yellow disks and become player 2. When it is a players turn to make a move, they must click the unfilled column that they would like to drop a disk in. This unfilled column will be highlighted grey. The disk representing their colour will appear in the last empty slot of the column and the other player can then make a move.


# Installation

# Documentation
## Directory Structure
	
## Major Classes and Methods

Major classes of the code used to put together the game application include Main, ConnectFourGUI, ConnectFourBoard, Controller and Button. The Main class includes methods getBoard(), getGUI() and main(), where main() runs the application and connects any adjustments in ConnectFourBoard to the ConnectFourGUI. The ConnectFourGUI includes a few update methods to change the state of the GUI when the game is being played. These methods include updateColumnButtons(), update_screen(), help_view(), play_game(), exit_game(), game_over(), reset_board(), draw_board() and create_text(). The ConnectFourBoard class is used to simulate the gameplay using methods that represents rules in the game such as drop(), check_for_win(), switch_turn() and is_game_over(). There are also helper functions for the board to work, which include check_win_at_position(), alternation(), valid_move(), get_drop_loc(), whos_turn and other_player(). The Controller class acts as a helper class for the GUI, which includes a method called wait_click() that detects clicking events and sends the x and y coordinates to the GUI. The Button class is used as a sensor object for the GUI, where the user can click their mouse and activate a change in the state of the GUI. The Button includes place(), change_colour() and reset_colour() to indicate which player's piece is on that button.

# Code Extension

4-to-Connect does not allow users to view the start page from the play page. To allow this, one can add to the update_screen method so that buttons can beplaced on the screen if self.isPlaying is True.

# Creators

# Individual Contributions

Hafsah Moalim:

I contributed to this project's code by creating the class skeleton for ConnectFourGUI and filling in some of its methods. In particular, I created the help page and start page for the game. In the init method for ConnectFourGUI, I used the Button class to  allow switching between the help and start page. I also made the create_text function  to make text appear on the screen. For the README file, I created section headers and  filled in some of the game controls and code extension sections.

# Licence
