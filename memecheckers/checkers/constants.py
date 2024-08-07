import pygame

import os



BOARD_SIZE = 700
INFO_PANEL_WIDTH = 300
WINDOW_WITH = BOARD_SIZE + INFO_PANEL_WIDTH
WINDOW_HEIGHT = BOARD_SIZE
WIDTH, HEIGHT = 700, 700
ROWS, COLS = 8, 8


SQUARE_SIZE =  WIDTH//COLS


FPS = 60

WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
BLACK = (255, 229, 204)
BLUE = (0, 0, 255)
# RED = (255, 0, 0)
RED = (204,102,0)
GRAY = (128, 128,128)


TIME_ICON = pygame.transform.scale(pygame.image.load(os.path.join('memecheckers/assets', 'time_icon.png')), (32, 32))
CROW = pygame.transform.scale(pygame.image.load(os.path.join('memecheckers/assets','crown.png')),(40,21))
WHITE_PIECE = pygame.transform.scale(pygame.image.load(os.path.join('memecheckers/assets', 'white_piece.png')),(52,52))
BLACK_PIECE = pygame.transform.scale(pygame.image.load(os.path.join('memecheckers/assets', 'black_piece.png')),(52,52))
TIME_ICON = pygame.transform.scale(pygame.image.load(os.path.join('memecheckers/assets', 'time_icon.png')), (32, 32))

WHITE_PIECE_SELECTED = pygame.transform.scale(pygame.image.load(os.path.join('memecheckers/assets', 'white_piece_selected.png')), (56, 56))
BLACK_PIECE_SELECTED = pygame.transform.scale(pygame.image.load(os.path.join('memecheckers/assets', 'black_piece_selected.png')), (56, 56))