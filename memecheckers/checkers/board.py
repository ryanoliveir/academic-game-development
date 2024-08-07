import pygame
from .constants import BLACK, RED, SELECTED_SOUND, WHITE, ROWS, COLS, SQUARE_SIZE
from .piece import Piece

class Board():
    def __init__(self):
        self.board = []
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0
        self.create_board()
    

    def draw_squares(self, window):
        window.fill(BLACK)

        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(window, RED, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)


        if row == ROWS - 1 or row == 0:
            piece.make_king()
            if piece.color == WHITE:
                self.white_kings += 1
            else: 
                self.red_kings += 1

    def get_piece(self, row, col):
        return self.board[row][col]


    def create_board(self):
         for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, WHITE))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, RED))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)
    
    def draw(self, window, selected_piece=None):
        self.draw_squares(window)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    if piece == selected_piece:
                        piece.draw(window, selected_piece)
                        
                    else:
                        piece.draw(window)

    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            
            if piece != 0:
                if piece.color == RED:
                    self.red_left -= 1
                else:
                    self.white_left -= 1
                    
    def winner(self):
        if self.red_left <= 0:
            return WHITE
        if self.white_left <= 0:
            return RED

    # def get_valid_moves(self, piece):
    #     moves = {}
    #     left = piece.col - 1
    #     right = piece.col + 1
    #     row = piece.row

    #     if piece.color == RED or piece.isKing:
    #         moves.update(self._traverse_left(row -1, max(row-3, -1), -1, piece.color, left))
    #         moves.update(self._traverse_right(row -1, max(row-3, -1), -1, piece.color, right))
    #     if piece.color == WHITE or piece.isKing:
    #         moves.update(self._traverse_left(row +1, min(row+3, ROWS), 1, piece.color, left))
    #         moves.update(self._traverse_right(row +1, min(row+3, ROWS), 1, piece.color, right))
    
    #     return moves

    
    # def get_valid_moves(self, piece):
    #     moves = {}
    #     left = piece.col - 1
    #     right = piece.col + 1
    #     row = piece.row

    #     if piece.isKing:
    #         moves.update(self._traverse(row - 1, -1, -1, piece.color))
    #         moves.update(self._traverse(row - 1, 1, -1, piece.color))
    #         moves.update(self._traverse(row + 1, -1, 1, piece.color))
    #         moves.update(self._traverse(row + 1, 1, 1, piece.color))
    #     else:
    #         if piece.color == RED:
    #             moves.update(self._traverse_left(row - 1, max(row - 3, -1), -1, piece.color, left))
    #             moves.update(self._traverse_right(row - 1, max(row - 3, -1), -1, piece.color, right))
    #         elif piece.color == WHITE:
    #             moves.update(self._traverse_left(row + 1, min(row + 3, ROWS), 1, piece.color, left))
    #             moves.update(self._traverse_right(row + 1, min(row + 3, ROWS), 1, piece.color, right))
    
        # return moves

    def get_valid_moves(self, piece):
        moves = {}
        if piece.isKing:
            moves.update(self._traverse_all_directions(piece))
        else:
            row, col = piece.row, piece.col
            if piece.color == RED:
                moves.update(self._traverse_left(row - 1, max(row - 3, -1), -1, piece.color, col - 1))
                moves.update(self._traverse_right(row - 1, max(row - 3, -1), -1, piece.color, col + 1))
            elif piece.color == WHITE:
                moves.update(self._traverse_left(row + 1, min(row + 3, ROWS), 1, piece.color, col - 1))
                moves.update(self._traverse_right(row + 1, min(row + 3, ROWS), 1, piece.color, col + 1))
        return moves

    def _traverse_all_directions(self, piece):
        moves = {}
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        for direction in directions:
            moves.update(self._traverse_direction(piece.row, piece.col, direction[0], direction[1], piece.color))
        return moves


    def _traverse_direction(self, row, col, row_step, col_step, color, skipped=[]):
        moves = {}
        last = []
        for i in range(1, ROWS):
            r = row + row_step * i
            c = col + col_step * i
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                break
            current = self.board[r][c]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, c)] = last + skipped
                else:
                    moves[(r, c)] = last
                if last:
                    temp_skipped = last.copy()
                    moves.update(self._traverse_direction(r + row_step, c + col_step, row_step, col_step, color, skipped=temp_skipped))
            elif current.color == color:
                break
            else:
                if last:
                    break
                else:
                    last = [current]
        return moves

    # def _traverse(self, start, direction, step, color):
    #     moves = {}
    #     last = []
    #     for r in range(start, ROWS if step == 1 else -1, step):
    #         c = direction
    #         while 0 <= c < COLS:
    #             current = self.board[r][c]
    #             if current == 0:
    #                 if last and not moves.get((r, c)):
    #                     moves[(r, c)] = last
    #                 elif not last:
    #                     moves[(r, c)] = []
    #             elif current.color != color:
    #                 if not last:
    #                     last = [current]
    #                 else:
    #                     break
    #             else:
    #                 break
    #             c += direction
    #         last = []
    #     return moves

    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break
            
            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last
                
                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)
                    moves.update(self._traverse_left(r+step, row, step, color, left-1,skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, color, left+1,skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            left -= 1
        
        return moves


    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLS:
                break
            
            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r,right)] = last + skipped
                else:
                    moves[(r, right)] = last
                
                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)
                    moves.update(self._traverse_left(r+step, row, step, color, right-1,skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, color, right+1,skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            right += 1
        
        return moves
