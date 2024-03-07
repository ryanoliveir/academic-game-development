import pygame
from .constants import RED, WHITE, SQUARE_SIZE

class Piece:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.isKing = False


        if self.color == RED:
            self.direction = -1
        else: 
            self.direction = 1

        self.x = 0
        self.y = 0
        define_position()

        def define_position():
            self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
            self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

        def make_king(self):
            self.isKing = True


        def draw(self, window):
            pygame.draw.circle(window, self.color, (self.x, self.y))