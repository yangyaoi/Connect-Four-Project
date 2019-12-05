# 4-to-Connect
4-to-Connect is a computer program created using python and Pygame. It is based on the classic game Connect 4.

# Game Description

# Game Controls
Users interact with the program with a mouse. Once 4-to-Connect is run, a user must press the start button in order to start game play. The first user to make a move will be player 1 and use red disks. The second user to make a move will use yellow disks and become player 2. When it is a players turn to make a move, they must click the unfilled column that they would like to drop a disk in. This unfilled column will be highlighted grey. The disk representing their colour will appear in the last empty slot of the column and the other player can then make a move.


# Installation

# Documentation
## Directory Structure
	
## Major Classes and Methods

# Code Extension

4-to-Connect does not allow users to view the start page from the play page. To allow this, one can add to the update_screen method so that buttons can beplaced on the screen if self.isPlaying is True.
## Change color of board
If you want to change the colour of the board, you can check the draw board method in the ConnectFourGUI class. In the third "For" loop, there is a function "pygame.draw.rect", you can change the argument of the function to change the colour of the board.
## Change color of disks
If you want to change the colour of disks, you can go into the class ConnectFourGui. There is a method "update screen". In the method, you should check into "elif self.isPlaying" statement, where there is a " if turn == P1" statement. Next, just change the argument of the function "pygame.draw.circle"
## Change rules of the game
The game rule is in the default setting, which is connect four. However, one can change the game rule with the method "alternation" in the class "ConnectFourBoard". In the method, there is a statement "for i in range(4)". We can change the game into "Connect 3","Connect 5" , "connect 6" by changing the integer in the function "range".For example, if I want to play "connect 3", I can just simply change the statement to "for i in range(3)".


# Creators

# Individual Contributions

Hafsah Moalim:

I contributed to this project's code by creating the class skeleton for ConnectFourGUI and filling in some of its methods. In particular, I created the help page and start page for the game. In the init method for ConnectFourGUI, I used the Button class to  allow switching between the help and start page. I also made the create_text function  to make text appear on the screen. For the README file, I created section headers and  filled in some of the game controls and code extension sections.

Yao Yang:

For coding the game, I cooperated with team member Hafsah to finish the GUI class. In particular, I created the game over page, which will show when the game ends. I also created a predictor for dropping chess pieces and also an indicator for the user's mouse movement(It tells the user which column they are at and where is the chess pieces dropping spot in that column ). Moreover, I also created a button class to simplify the code. For readme, I completed the code extension part, especially in how to change the colour of the board, chess pieces and also how to change the game rule.
# Licence
