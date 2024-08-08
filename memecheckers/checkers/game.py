import pygame
from .constants import (
    BOARD_SIZE, 
    GRAY, RED, 
    SELECTED_SOUND,
    START_SOUND, 
    WHITE, 
    BLUE, 
    SQUARE_SIZE, 
    WINDOW_HEIGHT, 
    WINDOW_WIDTH,
    CAPTURE_SOUND
)
from .board import Board
from .meme_handle import MemeHandler

class Game():
    def __init__(self, window): 
        self._init()
        self.window = window
        pygame.font.init()
        self.meme_handler = MemeHandler()
        self.font = pygame.font.SysFont('Arial', 24) 
        self.max_time = 30
        self.turn_start_time = pygame.time.get_ticks()


    def update(self):
        self.board.draw(self.window, self.selected)
        self.draw_valid_moves(self.valid_moves)
        self.update_timer() 
        self.draw_info_panel()
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = RED
        self.valid_moves = {}
        self.select_sound = SELECTED_SOUND
        self.capture_sound = CAPTURE_SOUND
        START_SOUND.play()
        self.turn_start_time = pygame.time.get_ticks()

    def reset(self):
       self._init()
    
    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        
        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            self.select_sound.play()
            return True
            
        return False 

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            captured_pieces = self.valid_moves[(row, col)]
            if captured_pieces:
                self.board.move(self.selected, row, col)
                self.board.remove(captured_pieces)
                self.capture_sound.play()  # Play capture sounds
                if len(captured_pieces) > 1:
                    self.meme_handler.play_meme(self.meme_handler.multi_capture_memes)
                else:
                    self.meme_handler.play_meme(self.meme_handler.capture_memes)
            else:
                self.board.move(self.selected, row, col)
            if self.selected.isKing:
                self.meme_handler.play_meme(self.meme_handler.queen_memes)
            self.change_turn()
            self.selected = None
        else:
            self.meme_handler.play_meme(self.meme_handler.invalid_move_memes) 
            return False
        return True


    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move

            pygame.draw.circle(self.window, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)


    def draw_info_panel(self):

        info_panel_x = BOARD_SIZE
        info_panel_width = WINDOW_WIDTH - BOARD_SIZE
        pygame.draw.rect(self.window, (173, 76, 38), (info_panel_x, 0, info_panel_width, WINDOW_HEIGHT))
        

        turn_text = self.font.render(f'Turn: {"Red" if self.turn == RED else "White"}', True, WHITE)
        red_left_text = self.font.render(f'Red Pieces Left: {self.board.red_left}', True, WHITE)
        white_left_text = self.font.render(f'White Pieces Left: {self.board.white_left}', True, WHITE)
        red_kings_text = self.font.render(f'Red Kings: {self.board.red_kings}', True, WHITE)
        white_kings_text = self.font.render(f'White Kings: {self.board.white_kings}', True, WHITE)
        timer_text = self.font.render(f'Time Left: {self.get_formatted_time()}s', True, WHITE)

        self.window.blit(turn_text, (info_panel_x + 10, 10))
        self.window.blit(red_left_text, (info_panel_x + 10, 50))
        self.window.blit(white_left_text, (info_panel_x + 10, 90))
        self.window.blit(red_kings_text, (info_panel_x + 10, 130))
        self.window.blit(white_kings_text, (info_panel_x + 10, 170))
        self.window.blit(timer_text, (info_panel_x + 10, 210))
        
    

    def update_timer(self):
        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - self.turn_start_time) / 1000  
        if elapsed_time >= self.max_time:
            self.change_turn()
    


    def get_remaining_time(self):
        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - self.turn_start_time) / 1000 
        remaining_time = max(0, self.max_time - elapsed_time)
        return int(remaining_time)
    
    def get_formatted_time(self):
        remaining_time = self.get_remaining_time()
        minutes = remaining_time // 60
        seconds = remaining_time % 60
        return f'{minutes:02}:{seconds:02}'

    def change_turn(self):
        self.valid_moves = {}
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED
        
        self.turn_start_time = pygame.time.get_ticks()
    