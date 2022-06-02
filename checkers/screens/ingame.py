import pygame
from checkers.constants import SQUARE_SIZE
from checkers.game import Game

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def run(win):
    run = True
    clock = pygame.time.Clock()
    game = Game(win)

    while run:
        clock.tick(60)

        if game.winner() != None:
            print(game.winner())
            return 'RESTART'

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'QUIT'
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()

