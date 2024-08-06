import pygame
from .constants import BOARD_SIZE, GRAY, RED, TIME_ICON, WHITE, BLUE, SQUARE_SIZE, WINDOW_HEIGHT, WINDOW_WITH
from .board import Board

class Game():
    def __init__(self, window): 
        self._init()
        self.window = window
        pygame.font.init()
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
            return True
            
        return False 
    

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
            self.selected = None
        else:
            return False

        return True


    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move

            pygame.draw.circle(self.window, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)


    def draw_info_panel(self):
        # Draw the info panel to the right of the board
        info_panel_x = BOARD_SIZE
        info_panel_width = WINDOW_WITH - BOARD_SIZE
        pygame.draw.rect(self.window, GRAY, (info_panel_x, 0, info_panel_width, WINDOW_HEIGHT))
        # Add text or other information display logic here


        turn_text = self.font.render(f'Turn: {"Red" if self.turn == RED else "White"}', True, WHITE)
        red_left_text = self.font.render(f'Red Pieces Left: {self.board.red_left}', True, WHITE)
        white_left_text = self.font.render(f'White Pieces Left: {self.board.white_left}', True, WHITE)
        red_kings_text = self.font.render(f'Red Kings: {self.board.red_kings}', True, WHITE)
        white_kings_text = self.font.render(f'White Kings: {self.board.white_kings}', True, WHITE)
        timer_text = self.font.render(f'Time Left: {self.get_formatted_time()}s', True, WHITE)
        # Blit text surfaces onto the info panel area
        self.window.blit(turn_text, (info_panel_x + 10, 10))
        self.window.blit(red_left_text, (info_panel_x + 10, 50))
        self.window.blit(white_left_text, (info_panel_x + 10, 90))
        self.window.blit(red_kings_text, (info_panel_x + 10, 130))
        self.window.blit(white_kings_text, (info_panel_x + 10, 170))
        self.window.blit(timer_text, (info_panel_x + 10, 210))
        # self.window.blit(TIME_ICON, (info_panel_x + 10, 210))
    

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
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED
        
        self.turn_start_time = pygame.time.get_ticks()
    