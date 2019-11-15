import pygame
import ConnectFourBoard as B
import ConnectFourGUI as G
import Controller as C

def Main:

    def __init__(self, GUI):
        self.board = GUI.Board
        self.GUI = GUI

    def getBoard(self):
        return self.board

    def getGUI(self):
        return self.GUI


def start_game(main, pygame):

    """Start the game and return the winner as string

    parameter:

    main (Main): Main instance
    pygame (pygame): initialized pygame

    Returns:

    string: P1 when player1 won, otherwise P2



    """


if __name__ == '__main__':
    pygame.init()
    main = Main(ConnectFourBoard.ConnectFourBoard(6,7))
    while not main.is_game_over():
        (x,y) = C.wait_click()
        column = C.get_column((x,y))

        if main.board.can_drop(column):
            main.board.drop(column)
            #updateGUI there

        if main.board.check_for_win():
            # show Win view for current player
            break

        main.board.turn = main.board.other_player()

    pygame.quit()
