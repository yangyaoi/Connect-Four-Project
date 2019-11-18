import pygame
from pygame.locals import *
import ConnectFourBoard as B
import ConnectFourGUI as G
import Controller as C

class Main:

    def __init__(self, GUI):
        self.board = GUI.board
        self.GUI = GUI

    def getBoard(self):
        return self.board

    def getGUI(self):
        return self.GUI

def wait_click():
    '''Get user input and return the x,y coordinates in pixels where user clicked'''
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit() # Force quit the game by closing window


        if event.type == MOUSEBUTTONDOWN:
            x, y = event.pos
            print("mouse clicked -> (" + str(x) + ", " + str(y) + ")")


if __name__ == '__main__':
    pygame = pygame.init()
    main = Main(G.ConnectFourGUI(B.ConnectFourBoard(6, 7)))
    while not main.board.is_game_over():

        (x,y) = wait_click()
        column = main.GUI.decide_column((x,y))

        if main.board.can_drop(column):
            main.board.drop(column)
            #updateGUI there

        if main.board.check_for_win():
            # show Winner view for current player
            main.GUI.game_over()
            pass

        main.board.turn = main.board.other_player()
    pygame.quit()
