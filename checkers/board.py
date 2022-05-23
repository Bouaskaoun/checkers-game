import pygame
from .constants import red,black,white,square_size,rows,columns
from .piece import Piece

class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.left_red = self.left_white = 12
        self.red_kings = self.white_kings = 0
        self.create_board()

    def draw_squares(self,win):
        win.fill(black)
        for row in range(rows):
            for col in range(row%2,columns,2):
                pygame.draw.rect(win,red,(row*square_size,col*square_size,square_size,square_size))

    def create_board(self):
        for row in range(rows):
            self.board.append([])
            for col in range(columns):
                if col % 2 == ((row + 1)% 2):
                    if row < 3:
                        self.board[row].append(Piece(row,col,white))
                    elif row > 4:
                        self.board[row].append(Piece(row,col,red))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self,win):
        self.draw_squares(win)
        for row in range(rows):
            for col in range(columns):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)
        
    def move(self,piece,row,col):
        self.board[piece.row][piece.column], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.column]
        piece.move(row,col)
        if row == rows or row == 0:
            piece.make_king()
            if piece.color == white:
                self.white_kings += 1
            else:
                self.red_kings +=1

    def get_piece(self,row,col):
        return self.board[row][col]