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
    def isClicked()->bool:
        return
if __name__ == "__main__":
    pygame.init()
    surface = pygame.display.set_mode((500,500))
    pygame.display.set_caption("4-to-Connect")
    running = True
    surface.fill((255,255,255))
    button = Button(surface,"quit",(0,0,255),(0,0,255),(0,0,0),100,100,50,20,"ellipse",20)
    button.place()
    pygame.display.update()
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                pygame.quit()
