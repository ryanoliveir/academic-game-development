# Game Development (Pygame)


## Useful Links

[Health Bars](https://www.youtube.com/watch?v=E82_hdoe06M)


```python

import pygame
from .constants import RED, WHITE, BLUE, SQUARE_SIZE, WINDOW_WIDTH, WINDOW_HEIGHT, BOARD_SIZE, GRAY, TIME_ICON
from .board import Board
from .meme_handle import MemeHandler

class Game:
    def __init__(self, window):
        self._init()
        self.window = window
        self.meme_handler = MemeHandler()
        pygame.font.init()
        self.font = pygame.font.SysFont('Arial', 24)  # Initialize font
        self.max_time = 30  # Maximum time per turn in seconds
        self.turn_start_time = pygame.time.get_ticks()  # Track when the turn started

        # Preload sound files
        self.select_sound = pygame.mixer.Sound('path/to/select_sound.wav')
        self.move_sound = pygame.mixer.Sound('path/to/move_sound.wav')
        self.capture_sound = pygame.mixer.Sound('path/to/capture_sound.wav')

        # Set sound volume if necessary (0.0 to 1.0)
        self.select_sound.set_volume(0.5)
        self.move_sound.set_volume(0.5)
        self.capture_sound.set_volume(0.5)

    def update(self):
        self.board.draw(self.window, self.selected)
        self.draw_valid_moves(self.valid_moves)
        self.update_timer()  # Update the timer
        self.draw_info_panel()  # Draw additional game info
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = RED
        self.valid_moves = {}
        self.turn_start_time = pygame.time.get_ticks()  # Reset the turn start time

    def reset(self):
        self._init()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        else:
            piece = self.board.get_piece(row, col)
            if piece != 0 and piece.color == self.turn:
                self.selected = piece
                self.valid_moves = self.board.get_valid_moves(piece)
                self.select_sound.play()  # Play select sound
                return True
        return False

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            captured_pieces = self.valid_moves[(row, col)]
            if captured_pieces:
                self.board.move(self.selected, row, col)
                self.board.remove(captured_pieces)
                self.capture_sound.play()  # Play capture sound
                if len(captured_pieces) > 2:
                    self.meme_handler.play_meme(self.meme_handler.multi_capture_memes)
                else:
                    self.meme_handler.play_meme(self.meme_handler.capture_memes)
            else:
                self.board.move(self.selected, row, col)
                self.move_sound.play()  # Play move sound
            if self.selected.isKing:
                self.meme_handler.play_meme(self.meme_handler.queen_memes)
            self.change_turn()
            self.selected = None  # Deselect after move
        else:
            self.meme_handler.play_meme(self.meme_handler.invalid_move_memes)  # Invalid move meme
            return False
        return True

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.window, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 15)

    def draw_info_panel(self):
        # Draw the info panel to the right of the board
        info_panel_x = BOARD_SIZE
        info_panel_width = WINDOW_WIDTH - BOARD_SIZE
        pygame.draw.rect(self.window, GRAY, (info_panel_x, 0, info_panel_width, WINDOW_HEIGHT))
        
        # Add text information
        turn_text = self.font.render(f'Turn: {"Red" if self.turn == RED else "White"}', True, WHITE)
        red_left_text = self.font.render(f'Red Pieces Left: {self.board.red_left}', True, WHITE)
        white_left_text = self.font.render(f'White Pieces Left: {self.board.white_left}', True, WHITE)
        red_kings_text = self.font.render(f'Red Kings: {self.board.red_kings}', True, WHITE)
        white_kings_text = self.font.render(f'White Kings: {self.board.white_kings}', True, WHITE)
        timer_text = self.font.render(f'Time Left: {self.get_formatted_time()}', True, WHITE)
        
        # Blit text surfaces onto the info panel area
        self.window.blit(turn_text, (info_panel_x + 10, 10))
        self.window.blit(red_left_text, (info_panel_x + 10, 50))
        self.window.blit(white_left_text, (info_panel_x + 10, 90))
        self.window.blit(red_kings_text, (info_panel_x + 10, 130))
        self.window.blit(white_kings_text, (info_panel_x + 10, 170))
        self.window.blit(TIME_ICON, (info_panel_x + 10, 210))
        self.window.blit(timer_text, (info_panel_x + 50, 210))

    def update_timer(self):
        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - self.turn_start_time) / 1000  # Convert to seconds
        if elapsed_time >= self.max_time:
            self.change_turn()

    def get_remaining_time(self):
        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - self.turn_start_time) / 1000  # Convert to seconds
        remaining_time = max(0, self.max_time - elapsed_time)
        return int(remaining_time)

    def get_formatted_time(self):
        remaining_time = self.get_remaining_time()
        minutes = remaining_time // 60
        seconds = remaining_time % 60
        return f'{minutes:02}:{seconds:02}'

    def change_turn(self):
        self.valid_moves = {}
        self.selected = None
        self.turn = WHITE if self.turn == RED else RED
        self.turn_start_time = pygame.time.get_ticks()  # Reset the turn start time

```