import pygame
from .constants import BLACK, RED, WHITE, ROWS, COLS, SQUARE_SIZE
from .piece import Piece

class Board():
    def __init__(self):
        self.board = []
        # self.selected = None
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


        if row == ROWS or row == 0:
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
                if col % 2 == (row + 1) % 2:
                    if row < 3:
                        self.board[row].append(Piece(row, col, WHITE))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, RED))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)
    
    def draw(self, window):
        self.draw_squares(window)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(window)

    

    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        if piece.color == RED or piece.isKing:
            moves.update(self._traverse_left(row -1, max(row-3, -1), -1, piece.color, left))
            moves.update(self._traverse_right(row -1, max(row-3, -1), -1, piece.color, right))
        if piece.color == WHITE or piece.isKing:
            moves.update(self._traverse_left(row +1, min(row+3, ROWS), 1, piece.color, left))
            moves.update(self._traverse_right(row +1, min(row+3, ROWS), 1, piece.color, right))
    
        return moves

    def _traverse_left(self, start, stop, step, color, left, skypped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break
            
            current = self.board[r][left]
            if current == 0:
                if skypped and not last:
                    break
                elif skypped:
                    moves[(r, left)]= last + skypped
                    pass
                else:
                    moves[(r,left)] = last

                if last:
                    if step == -1:
                        -1
                        row = max(r -3 , 0)
                    else:
                        row = min(r + 3, ROWS)

                    moves.update(self._traverse_left(r + step, row, step, color, left - 1, skypped=[]))
                    moves.update(self._traverse_right(r + step, row, step, color, left - 1, skypped=[]))
                    break
            else:
                last = [current]
            


            left -= 1

            return moves



    def _traverse_right(self, start, stop, step, color, right, skypped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLS:
                break
            
            current = self.board[r][right]
            if current == 0:
                if skypped and not last:
                    break
                elif skypped:
                    moves[(r, right)]= last + skypped
                    pass
                else:
                    moves[(r,right)] = last

                if last:
                    if step == -1:
                        -1
                        row = max(r -3 , 0)
                    else:
                        row = min(r + 3, ROWS)

                    moves.update(self._traverse_left(r + step, row, step, color, right - 1, skypped=[]))
                    moves.update(self._traverse_right(r + step, row, step, color, right +  1, skypped=[]))
                    break
            else:
                last = [current]
            


            right += 1

            return moves
