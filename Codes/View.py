from sys import exit
import pygame
from pygame.locals import *
from ConnectFourBoard import ConnectFourBoard
from tkinter import *
from Button import Button
from shapes import *

class View():
    """A class for the graphical user interface of 4-to-Connect"""
    BLUE = (0, 0, 255)
    LIGHT_BLUE = (0, 0, 128)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    LIGHT_GREEN = (110, 215, 180)


    WIDTH = 700
    HEIGHT = 700

    SCREEN = Screen(HEIGHT, WIDTH, LIGHT_GREEN, "start", pygame.display)
    


    def __init__(self, screen = SCREEN):
        """(ConnectFourGUI, ConnectFourBoard(int, int)) -> NoneType
        Set up the display window and the starting screen of the progam.
        REQ: board is a 6-by-7 ConnectFourBoard
        """
        self.SCREEN = screen
        self.SCREEN.set_scene("start")
        running = True
        while running:
            for event in pygame.event.get():
                # If the window is closed, exit the loop and go back to main
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_position = pygame.mouse.get_pos()
                    self.SCREEN.change_scene(mouse_position)
                    self.SCREEN.updateColumnButtons(mouse_position)
                    self.SCREEN.update_board(mouse_position)
                pygame.display.flip()

    def update_screen(self, scene, mouse_position = None):
        """(ConnectFourGUI, tuple) -> NoneType
        updates the screen when a button is clicked"""
        if scene == "start":
            self.SCREEN.change_scene(mouse_position)
        elif scene == "helpsave":
            pass
        elif scene == "help":
            pass
        elif scene == "playsave":
            pass
        elif scene == "play":
            pass
        elif scene == "exitwin":
            pass
        elif scene == "exittie":
            pass
        else: # just exit scene
            pass

    



if __name__ == "__main__":
    pygame.init()
    View = View()
    # Quit the game and exit the window
    pygame.quit()
    exit()
