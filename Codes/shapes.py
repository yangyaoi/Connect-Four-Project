import pygame
from pygame.locals import *
     
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
