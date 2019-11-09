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
        #check if the screen is on the gameover page
        self.isGameOver = False
        # Initilize the board
        self.board = board

        # Display the window for the program
        self.screen = pygame.display.set_mode((700, 500))
        self.screen.fill((110, 215, 180))
        pygame.display.set_caption("4-to-Connect")

        # Button font
        font = pygame.font.Font('freesansbold.ttf', 20)

        # Start button
        pygame.draw.ellipse(self.screen, (61, 89, 171), [300, 170, 100, 50])
        start_text = font.render("Start", True, (255, 255, 255), (61, 89, 171))
        starttextRect = start_text.get_rect()
        starttextRect.center = (350, 195)
        self.screen.blit(start_text, starttextRect)
        start_button = starttextRect

        # Help Button
        pygame.draw.ellipse(self.screen, (61, 89, 171), [300, 230, 100, 50])
        help_text = font.render("Help", True, (255, 255, 255), (61, 89, 171))
        helptextRect = help_text.get_rect()
        helptextRect.center = (350, 253)
        self.screen.blit(help_text, helptextRect)
        help_button = helptextRect

        # Exit Button
        pygame.draw.ellipse(self.screen, (61, 89, 171), [300, 290, 100, 50])
        exit_text = font.render("Exit", True, (255, 255, 255), (61, 89, 171))
        exittextRect = exit_text.get_rect()
        exittextRect.center = (350, 313)
        self.screen.blit(exit_text, exittextRect)
        exit_button = exittextRect

        # Create the title on the game start screen
        font = pygame.font.Font('freesansbold.ttf', 50)
        intro_text = font.render("4-to-Connect", True, (0, 0, 0),
                                 (110, 215, 180))
        introtextRect = intro_text.get_rect()
        introtextRect.center = (350, 125)
        self.screen.blit(intro_text, introtextRect)

        # Creators section
        font = pygame.font.Font('freesansbold.ttf', 20)
        creators_text = font.render("Creators", True, (0, 0, 0),
                                    (110, 215, 180))
        creatorstextRect = creators_text.get_rect()
        creatorstextRect.center = (620, 374)
        self.screen.blit(creators_text, creatorstextRect)
        # Names section
        name1_text = font.render("Calvin Vadivelu", True, (0, 0, 0),
                                 (110, 215, 180))
        name1textRect = name1_text.get_rect()
        name1textRect.center = (620, 394)
        self.screen.blit(name1_text, name1textRect)
        name2_text = font.render("Gen Tomita", True, (0, 0, 0),
                                 (110, 215, 180))
        name2textRect = name2_text.get_rect()
        name2textRect.center = (620, 414)
        self.screen.blit(name2_text, name2textRect)
        name3_text = font.render("Hafsah Moalim", True, (0, 0, 0),
                                 (110, 215, 180))
        name3textRect = name3_text.get_rect()
        name3textRect.center = (620, 434)
        self.screen.blit(name3_text, name3textRect)
        name4_text = font.render("Ilija Zivkovic", True, (0, 0, 0),
                                 (110, 215, 180))
        name4textRect = name1_text.get_rect()
        name4textRect.center = (630, 454)
        self.screen.blit(name4_text, name4textRect)
        name5_text = font.render("Yao Yang", True, (0, 0, 0), (110, 215, 180))
        name5textRect = name5_text.get_rect()
        name5textRect.center = (620, 474)
        self.screen.blit(name5_text, name5textRect)

        # Run game and make the neccessary changes to the screen when needed
        running = True
        while running:
            for event in pygame.event.get():
                # If the window is closed, exit the loop and go back to main
                if event.type == pygame.QUIT:
                    running = False
                # When one of the players clicks on the screen, get the mouse
                # position and update the screen to show their changes
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_position = pygame.mouse.get_pos()
                    self.update_screen(mouse_position)

                pygame.display.flip()

    def update_screen(self, mouse_position: tuple):
        """(ConnectFourGUI, tuple) -> NoneType
        updates any screen when a button is clicked"""
        #if game is on the game over page
        if self.isGameOver:
            #if quit button is clicked
            if (0<mouse_position[0]<200 and 0<mouse_position[2]<100):
                pygame.quit()
                self.isGameOver = False
            #if restart button is clicked
            if (500<mouse_position[0]<700 and 0<mouse_position[2]<100):
                self.reset_board()
                self.draw_board()
                self.isGameOver = False
        # if start button is clicked
        if (394 > mouse_position[0] > 306 and 217 > mouse_position[1] > 190):
            self.play_game()

        # if help button is clicked
        if (394 > mouse_position[0] > 306 and 274 > mouse_position[1] > 232):
            self.screen.fill((0, 0, 0))

        # if exit button is clicked
        if (394 > mouse_position[0] > 306 and 335 > mouse_position[1] > 295):
            self.exit_game()

    def start_game(self):
        """(ConnectFourGUI) -> NoneType
        updates the start screen"""
        return

    def game_over(self,winner:str):
        self.isGameOver = True
        self.screen.fill(WHITE)
        font = pygame.font.Font('freesansbold.ttf', 80)
        text = font.render("Winner: "+winner,True,(0,0,0))
        textPos = text.get_rect()
        textPos.center = (350,250)
        self.screen.blit(text,textPos)
        quitButton = Button(self.screen,"Quit",(0,0,255),(0,0,0),0,0,200,100,"rect",50)
        quitButton.place()
        restartButton = Button(self.screen,"Restart",(0,0,254),(0,0,0),500,0,200,100,"rect",50)
        restartButton.place()
    def play_game(self):
        """(ConnectFourGUI) -> NoneType
        updates the play screen"""
        self.draw_board()
        return

    def exit_game(self):
        """(ConnectFourGUI) -> NoneType
        updates the exit screen"""
        self.screen.fill((255, 255, 255))
        pygame.quit()
        exit()

        return

    def upate_board(self, board: ConnectFourBoard):
        """(ConnectFourGUI, ConnectFourBoard) -> NoneType
        updates the board"""
        return
    def reset_board(self):
        self.board = ConnestFourBoard
    def draw_board(self):
        """(ConnectFourGUI) -> NoneType
        Draws the board for use by the game
        To Do: 
         - Draw different coloured circles based on
        player input
         - Make board look better :(...
        """

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
        
if __name__ == "__main__":
    pygame.init()
    ConnectFourGUI = ConnextFourGui(ConnectFourBoard(6,7))
    # Quit the game and exit the window
    pygame.quit()
    exit()
