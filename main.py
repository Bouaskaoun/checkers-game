import pygame
from checkers.constants import WIDTH, HEIGHT
from checkers.game import Game
from checkers.screens import menu, ingame


WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')
pygame.display.set_icon(pygame.image.load('assets/chinese-checkers-32.png'))


def main():
    screen = menu.runMenu(WIN)
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if screen == 'Menu':
                screen = menu.runMenu(WIN)
            elif screen == 'INGAME':
                screen = ingame.runInGame(WIN)
            elif screen == 'QUIT':
                run = False
            

main()
