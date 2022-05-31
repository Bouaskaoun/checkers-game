import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, WHITE, BLACK, TITLE_FONT, BODY_FONT_SMALL, PADDING
from checkers.game import Game
from checkers.button import Button

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

buttons = [Button("START", "START", WIDTH / 2 + PADDING - 90, HEIGHT / 2 + PADDING * 2 + 100, BLACK, 0)]
def drawMenu(win):
    win.fill(WHITE)

    text = TITLE_FONT.render("Backgammon", 1, BLACK)
    win.blit(text, (round(WIDTH / 2) - round(text.get_width() / 2), 25))

    text = BODY_FONT_SMALL.render("v0.1", 1, BLACK)
    win.blit(text, (WIDTH - text.get_width() - PADDING, 150 - text.get_height() - PADDING))

    for b in buttons:
        b.draw(win)

    dices = pygame.image.load("assets/backgammon_ambiance3.png")
    win.blit(dices,(280,0))
    pygame.display.update()

def runMenu(window):
    display_screen = "MENU"
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for b in buttons:
                    if b.click(pos):
                        if b.button_id == "START":
                            return "INGAME"
        drawMenu(window)

def runInGame():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(60)

        if game.winner() != None:
            print(game.winner())
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()
    
    pygame.quit()


def main():
    screen = runMenu(WIN)
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(60)

        if game.winner() != None:
            print(game.winner())
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for b in buttons:
                    if b.click(pos):
                        if b.button_id == "START":
                            runInGame()

    pygame.quit()

main()
