import pygame
from .constants import RED, SQUARE_SIZE, GRAY, CROW

class Piece:
    PADDING = 17
    OUTLINE = 2

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
        self.define_position()

    def define_position(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

        
    def make_king(self):
        self.isKing = True


    def draw(self, window):
        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(window, GRAY, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(window, self.color, (self.x, self.y), radius)

        if self.isKing:
            window.blit(CROW, (self.x - CROW.get_width()//2, self.y - CROW.get_height()//2))


    def move(self, row, col):
        self.row = row
        self.col = col
        self.define_position()

    def __repr__(self):
        return str(self.color)