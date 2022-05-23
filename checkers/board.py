import pygame
from .constants import red,black,square_size,rows,columns

class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.left_red = self.left_white = 12
        self.red_kings = self.white_kings = 0

    def draw_squares(self,win):
        win.fill(black)
        for row in range(rows):
            for col in range(row%2,columns,2):
                pygame.draw.rect(win,red,(row*square_size,col*square_size,square_size,square_size))

    def create_piece():
        pass