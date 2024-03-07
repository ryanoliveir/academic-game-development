import pygame
from checkers.constants import WIDTH, HEIGHT, FPS
from checkers.board import Board
import sys

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))



pygame.display.set_caption('MemeChecks')



def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()




    while run:

        clock.tick(FPS)
        for event in pygame.event.get():
        
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()


        board.draw_squares(WINDOW)
        pygame.display.update()

main()


