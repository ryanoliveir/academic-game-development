import pygame

import os



BOARD_SIZE = 700
INFO_PANEL_WIDTH = 300
WINDOW_WIDTH = BOARD_SIZE + INFO_PANEL_WIDTH
WINDOW_HEIGHT = BOARD_SIZE
WIDTH, HEIGHT = 700, 700
ROWS, COLS = 8, 8

BACKGROUND_PRIMARY = (143, 75, 58)
SQUARE_SIZE =  WIDTH//COLS


FPS = 60

WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
BLACK = (202, 110, 60)
BLUE = (0, 0, 255)
# RED = (255, 0, 0)
RED = (221, 154, 103)
GRAY = (128, 128,128)


pygame.mixer.init()
pygame.font.init()



SELECTED_SOUND = pygame.mixer.Sound(os.path.join('memecheckers/assets', 'selected_sound.wav'))
CAPTURE_SOUND = pygame.mixer.Sound(os.path.join('memecheckers/assets', 'capture_song.wav'))
START_SOUND = pygame.mixer.Sound(os.path.join('memecheckers/assets', 'start_sound.wav'))


TIME_ICON = pygame.transform.scale(pygame.image.load(os.path.join('memecheckers/assets', 'time_icon.png')), (32, 32))
CROW = pygame.transform.scale(pygame.image.load(os.path.join('memecheckers/assets','crown.png')),(40,21))
WHITE_PIECE = pygame.transform.scale(pygame.image.load(os.path.join('memecheckers/assets', 'white_piece.png')),(52,52))
BLACK_PIECE = pygame.transform.scale(pygame.image.load(os.path.join('memecheckers/assets', 'black_piece.png')),(52,52))
TIME_ICON = pygame.transform.scale(pygame.image.load(os.path.join('memecheckers/assets', 'time_icon.png')), (32, 32))

WHITE_PIECE_SELECTED = pygame.transform.scale(pygame.image.load(os.path.join('memecheckers/assets', 'white_piece_selected.png')), (56, 56))
BLACK_PIECE_SELECTED = pygame.transform.scale(pygame.image.load(os.path.join('memecheckers/assets', 'black_piece_selected.png')), (56, 56))


WOOD_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join('memecheckers/assets','menu','wood_button.png')), (360, 360))
LOGO = pygame.transform.scale(pygame.image.load(os.path.join('memecheckers/assets', 'menu', 'troll-face.png')), (100,89))


FONT = pygame.font.Font(os.path.join('memecheckers/assets', 'fonts','SillerPersonalUse-9Y3wn.otf'), 60)