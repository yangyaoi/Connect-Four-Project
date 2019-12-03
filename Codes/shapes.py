import pygame
from pygame.locals import *
from ConnectFourBoard import ConnectFourBoard
from tkinter import *
     
# USE SCENE INSTEAD OF VIEW WHEN DESCRIBING DIFFERENT WAYS THE VIEW LOOKS LIKE
class Disk():
    """A class to represent a red or yellow disk in 4-to-Connect"""
    NUMOFDISKS = 0
    def __init__(self, width, pos_x, pos_y, line_thickness, colour, screen):
        """(int, int, int, int, (int, int, int)) -> NoneType
        Gets the width of the required disk along with
        the line_thickness which determines the fill of the disk using colour. 
        pos_x and pos_y give the center x and y coordinates of the disk.
        REQ: 500 >= width >= 0
        REQ: 500 >= pos_x >= 0
        REQ: 700 >= pos_y >= 0
        REQ: line_thickness >= 0
        REQ: colour can only contain ints 0-255
        """
        self._width = width
        self._x = pos_x
        self._y = pos_y
        self._line_thickness = line_thickness
        self._colour = colour
        self._screen = screen
        # Increase the amount of disks everytime one is created.
        self.NUMOFDISKS += 1

    def get_width(self):
        return self._width
    
    def set_width(self, width):
        self._width = width
        
    def get_x(self):
        return self._x
    
    def set_x(self, pos_x):
        self._x = pos_x    
        
    def get_y(self):
        return self._y
    
    def set_y(self, pos_y):
        self._y = pos_y  
        
    def get_colour(self):
        return self._colour
    
    def set_colour(self, colour):
        self._colour = colour
    
    def get_line_thickness(self):
        return self._line_thickness
    
    def set_line_thickness(self, line_thickness):
        self._line_thickness = line_thickness
        
    def place(self):
        cent = (self._x, self._y)
        pygame.draw.circle(self._screen, self._colour, cent, self._width)
        pygame.display.update()
    
    def _repr_(self):
        return [self._width, self._x, self._y, self._line_thickness, self._colour]


# Need textbox for buttons, screen etc
# MUST BE OBJECT
class TextBox():
    def __init__(self, text, pos_x, pos_y, re_font, size, screen, bold=False, colour = (0,0,0), italicize=False):
        self._text = text
        self._y = pos_y
        self._x = pos_x
        self._re_font = re_font
        self._size = size
        self._screen = screen
        self._bold = bold
        self._colour = colour
        self._italicize = italicize
        self._text_font = None
    
    #def create_text(self):
        #matched_font = pygame.font.match_font(self._re_font, self._bold, self._italicize)
        #if (matched_font is None):
            #matched_font = 'freesansbold.ttf'
        #self._text_font = pygame.font.Font(matched_font, self._size)
        
    #def place_text(self):
        ##if
        ## True is antialias 
        #render_text = self._text_font.render(self._text, True, self._colour)
        #renderedtextRect = render_text.get_rect()
        #renderedtextRect.center = (self._x, self._y)
        #self._screen.blit(render_text, renderedtextRect)
    
    def place(self):
        matched_font = pygame.font.match_font(self._re_font, self._bold, self._italicize)
        if (matched_font is None):
            matched_font = 'freesansbold.ttf'
        self._text_font = pygame.font.Font(matched_font, self._size)
        
        #if
        # True is antialias 
        render_text = self._text_font.render(self._text, True, self._colour)
        renderedtextRect = render_text.get_rect()
        renderedtextRect.center = (self._x, self._y)
        self._screen.blit(render_text, renderedtextRect)        
        
    
    def __repr__(self):
        pass

# Yao's button class
class Button():
    def __init__(self,surface,text:str,colour,indicatorColour,colourOfText,x,y,width,height,pattern,fontSize):
        self.text = text
        self.surface = surface
        self.colour = colour
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.pattern = pattern
        self.indicatorColour = indicatorColour
        self.colourOfText = colourOfText
        self.fontSize = fontSize
        self.clicked = False
        self.origin_colour = (colour[0],colour[1],colour[2])
        
    def is_clicked(self, mouse_position)->bool:
        if ((self.x + self.width) > mouse_position[0] > self.x and (self.y + self.height - 5) > mouse_position[1] > (self.y + self.height*0.5 - 5)):
            self.clicked = True
            return True
        return False

    def place(self)->None:
        if self.pattern == "rect":

            pygame.draw.rect(self.surface,self.colour,[self.x,self.y,self.width,self.height])
        elif self.pattern == "ellipse":
            pygame.draw.ellipse(self.surface,self.colour,[self.x,self.y,self.width,self.height])
        font = pygame.font.Font('freesansbold.ttf', self.fontSize)
        screen_text = font.render(self.text,True,self.colourOfText)
        textRect = screen_text.get_rect()
        textRect.center = (self.x+self.width/2,self.y+self.height/2)
        self.surface.blit(screen_text,textRect)
        
    def change_colour(self)->None:
        """
        change the color of button to indicatorcolour
        """
        self.colour = self.indicatorColour
       
        self.place()
    def reset_colour(self)->None:
        """
        chage the colour of button to origin colour
        """
        self.colour = self.origin_colour
        self.place()    
        
    def __repr__(self):
        pass


# composite
# Since there is only one screen, there will only be one instantiation of it
# in the view
class Screen():
    # STATIC: start, play, exit, help
    SCENE = ["start", "helpsave", "help", "playsave", "play", "exitwin", "exittie", "exit"]
    # differnet scenes:
    #      start, help(2), play(2), exit(3)
    

    def __init__(self, height, width, colour, scene, display):
        self._height = height # height of screen
        self._width = width # width of screen
        self._colour = colour # background colour
        self._scene = scene # different scenes
        self._display = pygame.display.set_mode((700, 700))
        self._start_button = Button(self._display, "Start", (61, 89, 171), (0, 0, 0), (255, 255, 255), 300, 170, 100, 50, "ellipse", 20)
        self._help_button = Button(self._display, "Help", (61, 89, 171), (0,0,0), (255,255,255), 300, 230, 100, 50, "ellipse", 20)
        self._exit_button = Button(self._display, "Exit", (61, 89, 171), (0,0,0), (255,255,255), 300, 290, 100, 50, "ellipse", 20)
        self.board = ConnectFourBoard(7, 6)
        self._saved_scenes = []
        self.indicateList = []
        self.columnsList = []#list of buttons represent columns.
        for i in range(7):
            self.columnsList.append(Button(self._display,str(i+1),(104,34,139),(191,62,255),(0,0,0),i*100+10,0,80,80,"ellipse",40))        
        
    def get_height(self):
        return self._height
    
    def get_width(self):
        return self._width
    
    def get_colour(self):
        return self._colour
    
    def get_current_scene(self):
        return self._scene
    
    def set_height(self, height):
        self._height = height
        
    def set_width(self, width):
        self._width = width
        
    def set_colour(self, colour):
        self._colour = colour
        
    def change_scene(self, mouse_position):
        if self._start_button.is_clicked(mouse_position):
            if self._scene == "helpsave":
                self.set_scene("playsave")
            else:
                self.update_board(mouse_position)
                self.updateColumnButtons(mouse_position)
                self.set_scene("play")
        if self._help_button.is_clicked(mouse_position):
            if self._scene == "play":
                self.set_scene("helpsave")
            else:
                self.set_scene("help")
        if self._exit_button.is_clicked(mouse_position):
            self.set_scene("exit")        
        
    # useful methods
    def set_scene(self, scene):
        """(Screen, str)-> NoneType
        
        """
        self._scene = scene
        # Display the window for the program
        self._display = pygame.display.set_mode((700, 700))
        self._display.fill((110, 215, 180))
        pygame.display.set_caption("4-to-Connect")

        # start scene
        if scene == "start":
            start_scene = Scene("start")
            
            self._start_button.x = 300
            self._start_button.y = 170
            start_scene.add_scene_obj(self._start_button)
            
            self._help_button.x = 300
            self._help_button.y = 230
            start_scene.add_scene_obj(self._help_button)
            
            self._exit_button.x = 300
            self._exit_button.y = 290
            start_scene.add_scene_obj(self._exit_button)
            

            # Create the title on the game start screen
            title = TextBox("4-to-Connect", 350, 125, 'default', 50, self._display)
            start_scene.add_scene_obj(title)
    
            # Creators Section
            creators = TextBox("Creators", 620, 374, 'default', 20, self._display)     
            start_scene.add_scene_obj(creators)
            
            calvin = TextBox("Calvin Vadivelu", 620, 394, 'default', 20, self._display)       
            start_scene.add_scene_obj(calvin)
            
            gen = TextBox("Gen Tomita", 620, 414, 'default', 20, self._display)      
            start_scene.add_scene_obj(gen)
            
            hafsah = TextBox("Hafsah Moalim", 620, 434, 'default', 20, self._display)     
            start_scene.add_scene_obj(hafsah)
            
            ilija = TextBox("Ilija Zivkovic", 620, 454, 'default', 20, self._display)
            start_scene.add_scene_obj(ilija)
            
            yao = TextBox("Yao Yang", 620, 474, 'default', 20, self._display)       
            start_scene.add_scene_obj(yao)
            
            start_scene.create_scene()

        # else if scene is a help type
            # NEED TO REMEMBER OLD PLAY
        elif scene == "helpsave":
            pass
        elif scene == "help":
            help_scene = Scene("help")
            
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
    
    
            help = TextBox("HELP", 350, 50, 'calibri', 50, self._display)
            help_scene.add_scene_obj(help)
    
            i = 0
            while (i < len(help_text)):
                if (help_text[i] == "How to Play" or help_text[i] == "Controls"):
                    help_scene.add_scene_obj(TextBox(help_text[i], 350, 100 + i*20, 'calibri', 20, self._display, True))
                else:
                    help_scene.add_scene_obj(TextBox(help_text[i], 350, 100 + i*20, 'calibri', 20, self._display))
                i += 1
    
    
            # Start button
            self._start_button.x = 50
            self._start_button.y = 425
            help_scene.add_scene_obj(self._start_button)
            
    
            # Exit button
            self._exit_button.x = 550
            self._exit_button.y = 425
            help_scene.add_scene_obj(self._exit_button)

            help_scene.create_scene()

        elif scene == "playsave":
            self._saved_scenes[-1].create_scene()
        elif scene == "play":
            play_scene = Scene("play")
            for i in range(7):
                play_scene.add_scene_obj(Button(self._display,str(i+1),(104,34,139),(191,62,255),(0,0,0),i*100+10,0,80,80,"ellipse",40))
        
            play_scene.create_scene()
            board = Board(8, 7, 0, 0, self._display)
            board.place()
            pygame.display.update()
        elif scene == "exitwin":
            pass
        elif scene == "exittie":
            pass
        else:
            exit_scene = Scene("exit")
            winner = TextBox("Winner: ", 350, 250, 'freesansbold.ttf', 80, self._display)
            exit_scene.add_scene_obj(winner)
            self._exit_button.x = 200
            self._exit_button.y = 100
            exit_scene.add_scene_obj(self._exit_button)
            self._start_button.x = 300
            self._start_button.y = 300
            exit_scene.add_scene_obj(self._start_button)
            exit_scene.create_scene()
      
    def update_board(self, mouse_position: tuple):
        """(Screen, tuple) -> NoneType
        updates the board for every move"""
        RED = (255, 0, 0)
        YELLOW = (255, 255, 0)
        SQUARESIZE = 100
        RADIUS = int(SQUARESIZE/2 - 5)
        #if game is on the playing(board) screen
        #Tempolary codes to update the model--------------------------
        column = self.decide_column(mouse_position)
        row = self.board.get_drop_loc(column)
        if self.board.valid_move(column,row):
            a = self.board.drop(column)
            print(self.board.board)
            loc = (int((column+0.5)*SQUARESIZE), int((row+1.5)*SQUARESIZE))
            print(2)
            if self.board.turn == "P1":
                
                pygame.draw.circle(self._display, RED, loc, RADIUS)
                print(3)
            else:
                pygame.draw.circle(self._display, YELLOW, loc, RADIUS)
                print(4)
            
            print(5)
        if self.board.check_for_win():
            print("ture")
            self.winner = self.board.other_player()
            self.set_scene("end")
        else:
            self.board.switch_turn()
        #-------------------------------------------------------------
        print(self.decide_column(mouse_position))
            
    def decide_column(self,mouse_position)->int:
        """
        return which column is mouse at
        """
        return int(mouse_position[0]/100)
    

    def updateColumnButtons(self,mouse_position):
        """
        updates screen when mouse is moved in playing stage
        """
            
        
        
        SQUARESIZE = 100
        RADIUS = int(SQUARESIZE/2 - 5)
        if self.indicateList != []:
            r = self.indicateList[-1][0]
            c = self.indicateList[-1][1]
            self.columnsList[c].reset_colour()
            if self.board.board[r][c] == "empty":
                loc = (int((c+0.5)*SQUARESIZE), int((r+1.5)*SQUARESIZE))
                pygame.draw.circle(self._display, (0,0,0), loc, RADIUS)
                
        column = self.decide_column(mouse_position)
        

        
        row_index = self.board.get_drop_loc(column)
        print(str(len(self.columnsList)) + "HERE")
        print(column)
            
        self.columnsList[column].change_colour()
        loc = (int((column+0.5)*SQUARESIZE), int((row_index+1.5)*SQUARESIZE))
        self.indicateList.append((row_index,column))
        pygame.draw.circle(self._display, (199,199,199), loc, RADIUS)

# Button is composite
class Scene():
    def __init__(self, scene_name):
        self._scene_name = scene_name
        self._scene_objs = [self._scene_name]
        self._num_of_objs = 1
        
    def get_name(self):
        return self._scene_name
    
    def set_name(self, scene_name):
        self._scene_name = scene_name
        self._scene_objs[0] = self._scene_name
        
    def add_scene_obj(self, obj):
        self._scene_objs.append(obj)
        self._num_of_objs += 1
        
    def remove_scene_obj(self, obj):
        self._scene_objs.remove(obj)
        
    # only things that can be updated
    def update_scene_obj(self, obj, pos_x = None, pos_y = None, colour = None):
        self.remove_scene_obj(obj)
        if type(obj) is Disk:
            obj.set_colour(colour)
        if type(obj) is Button:
            obj.x = pos_x
            obj.y = pos_y
        self._scene_objs.add_scene_obj(obj)
        
    def create_scene(self):
        for scene_obj in self._scene_objs[1:]:
            scene_obj.place()    

    def __repr__(self):
        return self._scene_objs
    
class Board():
    def __init__(self, num_rows, num_cols, length, width, display):
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._length = length
        self._width = width
        self._disks = []
        self._display = display
    
    def place(self):
        for c in range(self._num_cols):
            for r in range(self._num_rows):
                loc_size = (c*100, (r+1)*100, 100, 100)
                pygame.draw.rect(self._display, (0,0,255), loc_size)
                loc = (int((c+0.5)*100), int((r+1.5)*100))
                disk = Disk(int(100/2 - 5), loc[0], loc[1], 0, (0,0,0), self._display)
                self._disks.append(disk)
                disk.place()
        pygame.display.update()
