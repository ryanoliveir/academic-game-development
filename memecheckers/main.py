import pygame
from checkers.constants import WINDOW_WIDTH, WINDOW_HEIGHT, FPS, SQUARE_SIZE,RED
from checkers.game import Game
from checkers.menu import Menu
from checkers.winner import WinnerPanel
import sys

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))



pygame.display.set_caption('MemeChecks')


def get_row_col_from_mouse(position):
    x, y = position
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE

    return row, col


def check_click_area_is_valid(mouse_pos):
    if mouse_pos[0] <= 700:
        return True

    return False
    

def main(rerun=False):
    run = True
    if not rerun:
        menu = Menu(WINDOW)
        menu.run()


    clock = pygame.time.Clock()
    game = Game(WINDOW)
    

    while run:

        clock.tick(FPS)
        

        if game.winner() != None:
            winner_panel = WinnerPanel(WINDOW, game.winner())
            game.reset()
            game.meme_handler.play_meme(game.meme_handler.winn_memes)
            result = winner_panel.run()
    
            if result == 'play_again':
                run = False
                main(rerun=True)
                
            if result == 'menu':
                main(rerun=False)
                
        for event in pygame.event.get():
        
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                if (check_click_area_is_valid(mouse_position)):
                    row, col = get_row_col_from_mouse(mouse_position)
                    game.select(row, col)
            
                
        game.update()

main()
