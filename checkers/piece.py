import pygame
from .constants import red,grey,square_size

class Piece:
    padding = 10
    outline = 2
    def __init__(self,row,column,color):
        self.row = row
        self.column =column
        self.color = color
        self.king = False
        if self.color == red:
            self.direction = -1
        else:
            self.direction = 1
        self.x = 0
        self.y = 0
        self.calcul_position()
    def calcul_position(self):
        self.x = square_size * self.column + square_size // 2
        self.y = square_size * self.row + square_size // 2
    def make_king(self):
        self.king = True
    def draw(self,win):
        redius = square_size // 2 - self.padding
        pygame.draw.circle(win,grey,(self.x,self.y),redius + self.outline)
        pygame.draw.circle(win,self.color,(self.x,self.y),redius)
    def __repr__(self):
        return str(self.color)