import pygame
import ConnectFourBoard
import ConnectFourGUI

def Main:

    def __init__(Player1, Player2, GUI):
        self.board = GUI.Board
        self.player2 = GUI

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
