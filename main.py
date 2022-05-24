import pygame
from checkers.constants import width,hieght,square_size,rows,columns
from checkers.game import Game

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
    game = Game(window)
    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row,col = get_row_col(pos)



        game.update()

main()