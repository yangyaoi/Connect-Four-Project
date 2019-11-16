import pygame
from pygame.locals import *

from tkinter import *
     
# USE SCENE INSTEAD OF VIEW WHEN DESCRIBING DIFFERENT WAYS THE VIEW LOOKS LIKE
class Disk():
    """A class to represent a red or yellow disk in 4-to-Connect"""
    NUMOFDISKS = 0
    def __init__(width, pos_x, pos_y, line_thickness, colour):
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
        # Increase the amount of disks everytime one is created.
        NUMOFDISKS += 1

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


# Need textbox for buttons, screen etc
# MUST BE OBJECT
class TextBox():
    def __init__(text, pos_x, pos_y, re_font, size, screen, bold=False, colour = (0,0,0), italicize=False):
        self._text = text
        self._y = pos_y
        self._x = x
        self._re_font = re_font
    
    def create_text():
        matched_font = pygame.font.match_font(re_font, bold, italicize)
        if (matched_font is None):
            matched_font = 'freesansbold.ttf'
        text_font = pygame.font.Font(matched_font, size)
        
    def place_text():
        #if
        # True is antialias 
        render_text = text_font.render(text, True, colour)
        renderedtextRect = render_text.get_rect()
        renderedtextRect.center = (pos_x, pos_y)
        screen.blit(render_text, renderedtextRect)        

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


# composite
# Since there is only one screen, there will only be one instantiation of it
# in the view
class Screen():
    # STATIC: start, play, exit, help

    def __init__(self, height, width, colour):
        self._height = height # height of screen
        self._width = width # width of screen
        self._colour = colour # background colour
        
    def get_height():
        return self._height
    
    def get_width():
        return self._width
    
    def get_colour():
        return self._colour
    
    def set_height(self, height):
        self._height = height
        
    def set_width(self, width):
        self._width = width
        
    def set_colour(self, colour):
        self._colour = colour
        
    # useful methods
    def update_screen(self, scene):
        """(Screen, str)-> NoneType
        
        """
        pass
    
    
    # EQULAITY CHECK
    # USE FOR CHECKING WHICH SCENE IT IS
    # Difference between scenes:
    #      start scene has 4 dobjects - 1) TextBox for title, 2),3),4) start, exit, help buttons 5) TextBox for creators
    #      help scene has 8 objects - two are buttons and the rest are TextBox(s)
    #      play scene has 4 objects - 1) Board, 2) TextBox for "Player __, it is your turn!" 3) help button 4) exit button
    #      end scene has 6 objects - 1) "Player __ won!"/"Please play again"/"No one won", 2) buttons
    def __eq__(self, other):
        pass


# Button is composite

