from sys import exit
import pygame
from pygame.locals import *
from ConnectFourBoard import ConnectFourBoard


class ConnectFourGUI():
    """A class for the graphical user interface of 4-to-Connect"""

    def __init__(self, board: ConnectFourBoard(6, 7)):
        """(ConnectFourGUI, ConnectFourBoard(int, int)) -> NoneType
        Set up the display window and the starting screen of the progam.
        REQ: board is a 6-by-7 ConnectFourBoard
        """
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
        # if start button is clicked
        if (394 > mouse_position[0] > 306 and 217 > mouse_position[1] > 190):
            self.screen.fill((110, 215, 180))

        # if help button is clicked
        if (394 > mouse_position[0] > 306 and 274 > mouse_position[1] > 232):
            self.screen.fill((0, 0, 0))

        # if exit button is clicked
        if (394 > mouse_position[0] > 306 and 335 > mouse_position[1] > 295):
            self.screen.fill((255, 255, 255))

    def start_game(self):
        """(ConnectFourGUI) -> NoneType
        updates the start screen"""
        return

    def play_game(self):
        """(ConnectFourGUI) -> NoneType
        updates the play screen"""
        return

    def exit_game(self):
        """(ConnectFourGUI) -> NoneType
        updates the exit screen"""
        return

    def upate_board(self, board: ConnectFourBoard):
        """(ConnectFourGUI, ConnectFourBoard) -> NoneType
        updates the board"""
        return

if __name__ == "__main__":
    pygame.init()
    gui = ConnectFourGUI(ConnectFourBoard(6, 7))
    # Quit the game and exit the window
    pygame.quit()
    exit()
