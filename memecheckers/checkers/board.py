import pygame
from .constants import BLACK, RED, WHITE, ROWS, COLS, SQUARE_SIZE


class Board():
    def __init__(self):
        self.board = []
        self.selected = None
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0
    

    def draw_squares(self, window):
        window.fill(BLACK)

        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(window, RED, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def create_board(self):
        pass