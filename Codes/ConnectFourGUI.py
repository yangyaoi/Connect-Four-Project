from sys import exit
import pygame
from pygame.locals import *
from ConnectFourBoard import ConnectFourBoard
from tkinter import *
from Button import Button

class ConnectFourGUI():
    """A class for the graphical user interface of 4-to-Connect"""
    BLUE = (0, 0, 255)
    LIGHT_BLUE = (0, 0, 128)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    WHITE = (255,255,255)

    SQUARESIZE = 100
    NUM_COLS = 7
    NUM_ROWS = 6
    WIDTH = NUM_COLS*SQUARESIZE
    HEIGHT = (1+NUM_ROWS)*SQUARESIZE
    SIZE = (WIDTH, HEIGHT)

    RADIUS = int(SQUARESIZE/2 - 5)
    SCREEN = pygame.display.set_mode(SIZE)


    def __init__(self, board: ConnectFourBoard(6, 7)):
        """(ConnectFourGUI, ConnectFourBoard(int, int)) -> NoneType
        Set up the display window and the starting screen of the progam.
        REQ: board is a 6-by-7 ConnectFourBoard
        """
        self.indicateList = []
        self.columnsList = []#list of buttons represent columns.
        #check if the screen is on the gameover page
        self.isGameOver = False
        self.isPlaying = False
        # Initilize the board
        self.board = board
        #check if the screen is on the playing page
        self.isBoard = False

        # Temp attribute to hold who wins the game
        self.winner = ''

        # Display the window for the program
        self.screen = pygame.display.set_mode((700, 700))
        self.screen.fill((110, 215, 180))
        pygame.display.set_caption("4-to-Connect")

        # Start Button
        self.start_button = Button(self.screen, "Start", (61, 89, 171), (0, 0, 0), (255, 255, 255), 300, 170, 100, 50, "ellipse", 20)
        self.start_button.place()

        # Help Button
        self.help_button = Button(self.screen, "Help", (61, 89, 171), (0,0,0), (255,255,255), 300, 230, 100, 50, "ellipse", 20)
        self.help_button.place()

        # Exit Button
        self.exit_button = Button(self.screen, "Exit", (61, 89, 171), (0,0,0), (255,255,255), 300, 290, 100, 50, "ellipse", 20)
        self.exit_button.place()

        # Create the title on the game start screen
        create_text("4-to-Connect", 350, 125, 'default', 50, self.screen)

        # Creators Section
        create_text("Creators", 620, 374, 'default', 20, self.screen)
        create_text("Calvin Vadivelu", 620, 394, 'default', 20, self.screen)
        create_text("Gen Tomita", 620, 414, 'default', 20, self.screen)
        create_text("Hafsah Moalim", 620, 434, 'default', 20, self.screen)
        create_text("Ilija Zivkovic", 620, 454, 'default', 20, self.screen)
        create_text("Yao Yang", 620, 474, 'default', 20, self.screen)

        # Run game and make the neccessary changes to the screen when needed
        running = True
        while running:
            for event in pygame.event.get():
                # If the window is closed, exit the loop and go back to main
                if event.type == pygame.QUIT:
                    running = False
                # When one of the players clicks on the screen, get the mouse
                # position and update the screen to show their changes
                if event.type == pygame.MOUSEBUTTONDOWN :
                    mouse_position = pygame.mouse.get_pos()
                    self.update_screen(mouse_position)
                if self.isBoard:
                    mouse_position = pygame.mouse.get_pos()
                    self.updateColumnButtons(mouse_position)
                pygame.display.flip()

    def updateColumnButtons(self,mouse_position):
        """
        updates screen when mouse is moved in playing stage
        """
        if self.indicateList != []:
            r = self.indicateList[-1][0]
            c = self.indicateList[-1][1]
            self.columnsList[c].reset_colour()
            if self.board.board[r][c] == "empty":
                loc = (int((c+0.5)*self.SQUARESIZE), int((r+1.5)*self.SQUARESIZE))
                pygame.draw.circle(self.SCREEN, (0,0,0), loc, self.RADIUS)

        column = self.decide_column(mouse_position)



        row_index = self.board.get_drop_loc(column)

        self.columnsList[column].change_colour()
        loc = (int((column+0.5)*self.SQUARESIZE), int((row_index+1.5)*self.SQUARESIZE))
        self.indicateList.append((row_index,column))
        pygame.draw.circle(self.SCREEN, (199,199,199), loc, self.RADIUS)




    def update_screen(self, mouse_position: tuple):
        """(ConnectFourGUI, tuple) -> NoneType
        updates any screen when a button is clicked"""
        #if game is on the game over page
        if self.isGameOver:
            #if quit button is clicked
            if (0<mouse_position[0]<200 and 0<mouse_position[1]<100):
                pygame.quit()
                self.isGameOver = False
            #if restart button is clicked
            if (500<mouse_position[0]<700 and 0<mouse_position[1]<100):
                self.reset_board()
                self.screen.fill(self.BLUE)
                self.draw_board()
                self.isGameOver = False
        #if game is on the playing(board) screen
        elif self.isPlaying:
            #Tempolary codes to update the model--------------------------
            column = self.decide_column(mouse_position)
            row = self.board.get_drop_loc(column)
            if self.board.valid_move(column,row):
                a = self.board.drop(column)
                print(self.board.board)
                loc = (int((column+0.5)*self.SQUARESIZE), int((row+1.5)*self.SQUARESIZE))
                print(2)
                if self.board.turn == "P1":

                    pygame.draw.circle(self.SCREEN, self.RED, loc, self.RADIUS)
                    print(3)
                else:
                    pygame.draw.circle(self.SCREEN, self.YELLOW, loc, self.RADIUS)
                    print(4)

                print(5)
            if self.board.check_for_win():
                print("ture")
                self.winner = self.board.other_player()
                self.game_over(self.winner)
            else:
                self.board.switch_turn()
            #-------------------------------------------------------------
            '''
            Please write codes to actually put stone in the view.
            self.board.whos_turn shows who current player is.
            Due to the bugs in check_for_win function, it will finish the game
            in some occations.
            '''
            print(self.decide_column(mouse_position))
        else:
            # if start button is clicked
            if (self.start_button.x + self.start_button.width > mouse_position[0] > self.start_button.x and (self.start_button.y + self.start_button.height - 5) > mouse_position[1] > (self.start_button.y + self.start_button.height*0.5 - 5)):
                self.start_button.clicked = True
                self.play_game()

            # if help button is clicked
            if (self.help_button.x + self.help_button.width > mouse_position[0] > self.help_button.x and (self.help_button.y + self.help_button.height - 5) > mouse_position[1] > (self.help_button.y + self.help_button.height*0.5 - 5)):
                self.help_button.clicked = True
                self.help_view()

            # if exit button is clicked
            if (self.exit_button.x + self.exit_button.width > mouse_position[0] > self.exit_button.x and (self.exit_button.y + self.exit_button.height - 5) > mouse_position[1] > (self.exit_button.y + self.exit_button.height*0.5 - 5)):
                self.exit_button.clicked = True
                self.exit_game()

    def decide_column(self,mouse_position)->int:
        """
        return which column is mouse at
        """
        return int(mouse_position[0]/100)

    def start_game(self):
        """(ConnectFourGUI) -> NoneType
        updates the start screen"""
        return

    def help_view(self):
        """(ConnectFourGUI) -> NoneType
        Updates the display to show the help screen when a user presses
        the help button.
        """
        self.screen.fill((110, 215, 180))
        # Help text
        help_text = []
        help_text.append("4-to-Connect is a computer program based on the classic game Connect 4. To begin")
        help_text.append("playing, press the start button.")
        help_text.append("")
        help_text.append("How to Play")
        help_text.append("This game requires two players, a 7x6 board and disks that are either red or yellow.")
        help_text.append("Players take turns dropping disks into columns until a player wins or no more moves")
        help_text.append("are possible. To win, a player must have made 4 disks of their colour be in a row,")
        help_text.append("column or diagonal. The game is a tie when all 42 slots are filled with disks.")
        help_text.append("")
        help_text.append("Controls")
        help_text.append("The first player to make a move will be player 1 and have a red disk. When it is your")
        help_text.append("turn to make a move, click the unfilled column that you would like to drop a disk in. ")
        help_text.append("The disk representing your colour will appear in the last empty slot of the column")
        help_text.append("and the other player can then make a move.")

        # create help text and add it to the screen
        create_text("HELP", 350, 50, 'calibri', 50, self.screen, True)

        i = 0
        while (i < len(help_text)):
            if (help_text[i] == "How to Play" or help_text[i] == "Controls"):
                create_text(help_text[i], 350, 100 + i*20, 'calibri', 20, self.screen, True)
            else:
                create_text(help_text[i], 350, 100 + i*20, 'calibri', 20, self.screen)
            i += 1


        # create start and help buttons
        self.start_button = Button(self.screen, "Start", (61, 89, 171), (0,0,0), (255,255,255), 50, 425, 100, 50, "ellipse", 20)
        self.exit_button = Button(self.screen, "Exit", (61, 89, 171), (0,0,0), (255,255,255), 550, 425, 100, 50, "ellipse", 20)
        
        # place the buttons on the screen
        self.start_button.place()
        self.exit_button.place()
        
        # update display to show the help view
        pygame.display.update()
            

    def game_over(self,winner:str):
        self.isBoard = False
        self.isGameOver = True
        self.screen.fill(self.WHITE)
        font = pygame.font.Font('freesansbold.ttf', 80)
        text = font.render("Winner: "+winner,True,(0,0,0))
        textPos = text.get_rect()
        textPos.center = (350,250)
        self.screen.blit(text,textPos)
        quitButton = Button(self.screen,"Quit",(0,0,255),(0,0,0),(0,0,0),0,0,200,100,"rect",50)
        quitButton.place()
        restartButton = Button(self.screen,"Restart",(0,0,254),(0,0,0),(0,0,0),500,0,200,100,"rect",50)
        restartButton.place()
    def play_game(self):
        """(ConnectFourGUI) -> NoneType
        updates the play screen"""
        self.isPlaying = True
        self.draw_board()
        return

    def exit_game(self):
        """(ConnectFourGUI) -> NoneType
        updates the exit screen"""
        pygame.quit()
        exit()
        return

    def update_board(self, board: ConnectFourBoard):
        """(ConnectFourGUI, ConnectFourBoard) -> NoneType
        updates the board"""
        return
    def reset_board(self):

        self.board = ConnectFourBoard(6,7)
        self.isGameOver = False

    def draw_board(self):
        """(ConnectFourGUI) -> NoneType
        Draws the board for use by the game
        To Do:
         - Draw different coloured circles based on
        player input
         - Make board look better :(...
        """
        self.screen.fill(self.BLUE)
        #draw 5 buttons represent number of columns.
        self.isBoard = True


        for i in range(7):
            self.columnsList.append(Button(self.screen,str(i+1),(104,34,139),(191,62,255),(0,0,0),i*self.SQUARESIZE+10,0,80,80,"ellipse",40))

        for buttons in self.columnsList:
            buttons.place()
        for c in range(self.NUM_COLS):
            for r in range(self.NUM_ROWS):
                loc_size = (c*self.SQUARESIZE, (r+1)*self.SQUARESIZE, self.SQUARESIZE, self.SQUARESIZE)
                pygame.draw.rect(self.SCREEN, self.BLUE, loc_size)
                loc = (int((c+0.5)*self.SQUARESIZE), int((r+1.5)*self.SQUARESIZE))
                pygame.draw.circle(self.SCREEN, self.BLACK, loc, self.RADIUS)

        # for c in range(self.NUM_COLS):
        #     for r in range(self.NUM_ROWS):
        #         if self.board[r][c] == 1:
        #             loc = (int((c+0.5)*self.SQUARESIZE), int((r+1.5)*self.SQUARESIZE))
        #             pygame.draw.circle(self.SCREEN, self.RED, loc, self.RADIUS)
        #         elif self.board[r][c] == -1:
        #             loc = (int((c+0.5)*self.SQUARESIZE), int((r+1.5)*self.SQUARESIZE))
        #             pygame.draw.circle(self.SCREEN, self.YELLOW, loc, self.RADIUS)
        pygame.display.update()


def create_text(text, pos_x, pos_y, re_font, size, screen, bold=False, colour = (0,0,0), italicize=False):
    """Gives something that you can put right away on board"""


    matched_font = pygame.font.match_font(re_font, bold, italicize)
    if (matched_font is None):
        matched_font = 'freesansbold.ttf'
    text_font = pygame.font.Font(matched_font, size)

    # True is antialias
    render_text = text_font.render(text, True, colour)
    renderedtextRect = render_text.get_rect()
    renderedtextRect.center = (pos_x, pos_y)
    screen.blit(render_text, renderedtextRect)


if __name__ == "__main__":
    pygame.init()
    ConnectFourGui = ConnectFourGUI(ConnectFourBoard(6,7))
    # Quit the game and exit the window
    pygame.quit()
    exit()
