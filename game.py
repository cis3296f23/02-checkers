# game.py
# game file that holds game logic, game class has Main_Board object
# code from reference repo: https://github.com/techwithtim/Python-Checkers-AI

import pygame
from constants import RED, WHITE, YELLOW, SQUARE_SIZE
from Main_Board import Main_Board

class Game: # game class to handle game logic, color represents board color chosen by user
    def __init__(self, win, color):
        self.turn_start_time = pygame.time.get_ticks()
        self.turn_timeout = 5000  # 5 seconds per turn
        self.win = win
        self.color = color
        self.selected = None
        self.board = Main_Board(self.color)
        self.turn = RED
        self.valid_moves = {}
        
    def check_turn_timeout(self):
        elapsed_time = pygame.time.get_ticks() - self.turn_start_time
        print(f"Elapsed Time: {elapsed_time} ms")
        if elapsed_time > self.turn_timeout:
            self.change_turn()
            
    def update(self): # update board to show current board
        self.board.draw(self.win)
        self.show_available_moves(self.valid_moves)
        self.check_turn_timeout()
        pygame.display.update()
        
    def winner(self): # if winner has been found, return winner
        return self.board.winner()

    def select(self, row, col):
        if self.selected:
            result = self.move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)

        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True

        return False

    def move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves.get((row, col))
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
            self.turn_start_time = pygame.time.get_ticks()  # Reset the turn timer
            return True

        return False

    def show_available_moves(self, moves): # show available moves for selected piece
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, YELLOW, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)

    def change_turn(self): # change turn to other player/color
        self.valid_moves = {}
        self.turn_start_time = pygame.time.get_ticks()  # Reset the turn timer
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED

    def get_board(self): # return current board
        return self.board

    def ai_move(self, board): # move AI piece
        self.board = board
        self.change_turn()