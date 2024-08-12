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
    CAPTURE_SOUND,
    FONT_INFO_PANEL_DATA,
    FONT_INFO_PANEL_LABEL,
    FONT_INFO_PANEL_LABEL_SMALL,
    FONT_INFO_PANEL_DATA_SMALL
)
from .board import Board
from .meme_handle import MemeHandler

class Game():
    def __init__(self, window): 
        self._init()
        self.window = window
        pygame.font.init()
        self.meme_handler = MemeHandler()
        self.font_info_label = FONT_INFO_PANEL_LABEL
        self.font_info_data = FONT_INFO_PANEL_DATA
        self.font_info_label_small = FONT_INFO_PANEL_LABEL_SMALL
        self.font_info_data_small = FONT_INFO_PANEL_DATA_SMALL
        self.info_panel_padding = 50
        self.max_time = 30
        self.turn_start_time = pygame.time.get_ticks()


    def update(self):
        self.board.draw(self.window, self.selected)
        # self.draw_valid_moves(self.valid_moves)
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
       
    def winner(self):
        return self.board.winner()
    
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
    
        # Render the text elements
        turn_text_label = self.font_info_label.render('Turno:', True, WHITE)
        turn_text_data = self.font_info_data.render(f'{"Preto" if self.turn == RED else "Branco"}', True, WHITE)
        black_left_text = self.font_info_label.render(f'Pretas: {self.board.red_left}', True, WHITE)
        white_left_text = self.font_info_label.render(f'Brancas: {self.board.white_left}', True, WHITE)
        black_kings_text = self.font_info_label_small.render(f'Damas: {self.board.red_kings}', True, WHITE)
        white_kings_text = self.font_info_label_small.render(f'Damas: {self.board.white_kings}', True, WHITE)
        timer_text = self.font_info_label.render(f'Tempo: {self.get_formatted_time()}', True, WHITE)
    
        # Calculate the total height of all the text elements combined
        total_height = (
            turn_text_label.get_height() +
            black_left_text.get_height() +
            black_kings_text.get_height() +
            white_left_text.get_height() +
            white_kings_text.get_height() +
            timer_text.get_height() +
            (5 * 10)  # Adding spacing between elements
        )
    
        # Calculate the starting y position to center the text block vertically
        start_y = (WINDOW_HEIGHT - total_height) // 2
    
        # Draw the text elements centered vertically
        current_y = start_y
        self.window.blit(turn_text_label, (info_panel_x + self.info_panel_padding, current_y))
        self.window.blit(turn_text_data, (info_panel_x + self.info_panel_padding + 90, current_y))
        current_y += turn_text_label.get_height() + 10
        self.window.blit(black_left_text, (info_panel_x + self.info_panel_padding, current_y))
        current_y += black_left_text.get_height() + 10
        self.window.blit(black_kings_text, (info_panel_x + self.info_panel_padding, current_y))
        current_y += black_kings_text.get_height() + 10
        self.window.blit(white_left_text, (info_panel_x + self.info_panel_padding, current_y))
        current_y += white_left_text.get_height() + 10
        self.window.blit(white_kings_text, (info_panel_x + self.info_panel_padding, current_y))
        current_y += white_kings_text.get_height() + 10
        self.window.blit(timer_text, (info_panel_x + self.info_panel_padding, current_y))
        
    

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
    