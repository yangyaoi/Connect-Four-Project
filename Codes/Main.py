import pygame
import ConnectFourBoard
import ConnectFourGUI

def Controller:

    def __init__(Player1, Player2, GUI):
        self.board = GUI.Board
        self.player2 = GUI

    def getBoard(self):
        return self.board

    def getGUI(self):
        return self.GUI

    def wait_click(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit() # Force quit the game by closing window

            # マウスクリック時の動作
            if event.type == MOUSEBUTTONDOWN:
                x, y = event.pos
                print("mouse clicked -> (" + str(x) + ", " + str(y) + ")") #Temp output to check the clicked position



def start_game(main, pygame):

    """Start the game and return the winner as string

    parameter:

    main (Main): Main instance
    pygame (pygame): initialized pygame

    Returns:

    string: P1 when player1 won, otherwise P2



    """

    board = main.board

    while not board.check_for_win():
        key = pygame.key.get_pressed

        while not key[K_S] or not key[K_DOWN]:
            if board.whos_turn == "P1"
                if keys[K_LEFT]:
                    board.move_left
                elif keys[K_RIGHT]:
                    board.move_right
                #UPdating screen for user input is required.
            else:
                if keys[K_A]:
                    board.move_left
                elif keys[K_D]:
                    board.move_right

            main.GUI.update_screen() #The timing of updating screen has to be reconsidered.
            keys = pygame.key.get_pressed()

        board.drop()
        board.turn = board.other_player()

    return board.other_player
