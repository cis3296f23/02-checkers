import pygame
from constants import RED, BLACK, SQUARE_SIZE,COLS
from pieces import Piece


ROWS = 8

class MAIN_Board:
    def __init__(self, color1, color2, board_color):
        self.color1 = color1
        self.color2 = color2
        self.board_color = board_color
        self.board = [[None] * ROWS for _ in range(ROWS)]
        self.initialize_pieces()

        self.red_left = self.black_left = 12
        self.red_kings = self.white_kings = 0

    def initialize_pieces(self):
        for row in range(3):
            for col in range(ROWS):
                if (row + col) % 2 == 1:
                    self.board[row][col] = Piece(self.color1, row, col)

        for row in range(5, ROWS):
            for col in range(ROWS):
                if (row + col) % 2 == 1:
                    self.board[row][col] = Piece(self.color2, row, col)
                    
    def get_all_pieces(self, color):
        return [piece for row in self.board for piece in row if piece and piece.color == color]

    
    def get_all_pieces(self, color):
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color:
                    pieces.append(piece)
        return pieces
    
    
    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        if row == ROWS - 1 or row == 0:
            piece.make_king()
            if piece.color == BLACK:
                self.white_kings += 1
            else:
                self.red_kings += 1 

    def get_piece(self, row, col):
        return self.board[row][col]
    
    
    def draw_board(self, win):
        win.fill(self.board_color)

        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                #This draws the board color 
                pygame.draw.rect(win, RED, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

            for col in range((row + 1) % 2, ROWS, 2):
                #This draws the board color 
                pygame.draw.rect(win, BLACK, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                

    def draw_pieces(self, win):
        for row in range(ROWS):
            for col in range(ROWS):
                piece = self.board[row][col]
                if piece:
                    piece.draw(win)

    def place_piece(self, row, col, piece):
        self.board[row][col] = piece
        
        
    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == RED:
                    self.red_left -= 1
                else:
                    self.black_left -= 1


    def winner(self):
        if self.red_left <= 0:
            return BLACK
        elif self.black_left <= 0:
            return RED
        
        return None 
    
    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        if piece.color == RED or piece.king:
            moves.update(self._traverse_left(row - 1, max(row - 3, -1), -1, piece.color, left))
            moves.update(self._traverse_right(row - 1, max(row - 3, -1), -1, piece.color, right))
        if piece.color == BLACK or piece.king:
            moves.update(self._traverse_left(row + 1, min(row + 3, ROWS), 1, piece.color, left))
            moves.update(self._traverse_right(row + 1, min(row + 3, ROWS), 1, piece.color, right))

        return moves

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