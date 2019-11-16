import pygame
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



if __name__ == '__main__':
    pygame.init()
    main = Main(G.ConnectFourGUI(B.ConnectFourBoard(6, 7)))
    while not main.board.is_game_over():
        (x,y) = C.wait_click()
        column = main.GUI.decide_column((x,y))

        if main.board.can_drop(column):
            main.board.drop(column)
            #updateGUI there

        if main.board.check_for_win():
            # show Winner view for current player
            pass
        main.board.turn = main.board.other_player()

    pygame.quit()
