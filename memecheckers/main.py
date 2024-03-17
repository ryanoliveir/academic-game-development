import pygame
from checkers.constants import WIDTH, HEIGHT, FPS, SQUARE_SIZE
from checkers.board import Board
import sys

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))



pygame.display.set_caption('MemeChecks')


def get_row_col_from_mouse(position):
    x, y = position
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE

    return row, col


def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()

    piace = board.get_piece(0,1)
    board.move(piace, 4,1)

    while run:

        clock.tick(FPS)
        for event in pygame.event.get():
        
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(mouse_position)
                piace = board.get_piece(row, col)
                board.move(piace, 4,3)

        board.draw(WINDOW)
        pygame.display.update()

main()


