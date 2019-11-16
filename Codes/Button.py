from sys import exit
import pygame
from pygame.locals import *

from tkinter import *
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