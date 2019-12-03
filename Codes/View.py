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
    


    def __init__(self):
        """(ConnectFourGUI, ConnectFourBoard(int, int)) -> NoneType
        Set up the display window and the starting screen of the progam.
        REQ: board is a 6-by-7 ConnectFourBoard
        """
        self.SCREEN.set_scene("start")
        running = True
        while running:
            for event in pygame.event.get():
                # If the window is closed, exit the loop and go back to main
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_position = pygame.mouse.get_pos()
                    print(self.SCREEN.get_scene_name())
                    self.SCREEN.change_scene(mouse_position)
                    print(self.SCREEN.get_scene_name())
                    if self.SCREEN.get_scene_name() == "play":
                        #pass
                        self.SCREEN.drawn_board.update_board(mouse_position)
                        self.SCREEN.drawn_board.updateColumnButtons(mouse_position)
                    if self.SCREEN.drawn_board.isBoard and self.SCREEN.get_scene_name() == "play":
                        #self.SCREEN.change_scene(mouse_position)
                        if self.SCREEN.drawn_board.winner != '':
                            self.SCREEN.set_scene("end")
                            self.SCREEN.drawn_board.winner = ''
                            print(self.SCREEN.get_scene_name())
                            self.SCREEN.drawn_board.isBoard = False
                #self.SCREEN.change_scene(mouse_position)
                pygame.display.flip()

    def update_screen(self, scene, mouse_position = None):
        """(ConnectFourGUI, tuple) -> NoneType
        updates the screen when a button is clicked"""
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
            if (394 > mouse_position[0] > 306 and 217 > mouse_position[1] > 190):
                self.start_button.clicked = True
                self.play_game()

            # if help button is clicked
            if (394 > mouse_position[0] > 306 and 274 > mouse_position[1] > 232):
                self.help_button.clicked = True
                self.help_view()

            # if exit button is clicked
            if (394 > mouse_position[0] > 306 and 335 > mouse_position[1] > 295):
                self.exit_button.clicked = True
                self.exit_game()


    



if __name__ == "__main__":
    pygame.init()
    View = View()
    # Quit the game and exit the window
    pygame.quit()
    exit()
