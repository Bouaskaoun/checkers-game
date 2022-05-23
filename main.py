import pygame
from checkers.constants import width,hieght,square_size,rows,columns
from checkers.board import Board

pygame.init()

window = pygame.display.set_mode((width,hieght))
pygame.display.set_caption('Checkers')


def get_row_col(pos):
    x,y = pos
    row = y // square_size
    col = x // square_size
    return row,col

def main():
    clock = pygame.time.Clock()
    board = Board()
    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row,col = get_row_col(pos)
                piece = board.get_piece(row,col)
                board.move(piece,4,3)


        board.draw(window)
        pygame.display.update()

main()