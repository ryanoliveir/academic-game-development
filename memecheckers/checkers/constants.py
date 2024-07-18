import pygame
import os

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE =  WIDTH//COLS


FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLACK = (255, 229, 204)
BLUE = (0, 0, 255)
# RED = (255, 0, 0)
RED = (204,102,0)
GRAY = (128, 128,128)


CROW = pygame.transform.scale(pygame.image.load(os.path.join('memecheckers/assets','crown.png')),(44,25))

