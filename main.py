import pygame
from checkers.constants import width,hieght
from checkers.board import Board

pygame.init()

window = pygame.display.set_mode((width,hieght))
pygame.display.set_caption('Checkers')


def main():
    clock = pygame.time.Clock()
    board = Board()
    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        board.draw_squares(window)
        pygame.display.update()

main()