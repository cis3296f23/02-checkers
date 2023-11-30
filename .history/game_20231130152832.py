# game.py
# game file that holds game logic, game class has Main_Board object
# code from reference repo: https://github.com/techwithtim/Python-Checkers-AI

import pygame
from constants import RED, WHITE, YELLOW, SQUARE_SIZE
from Main_Board import Main_Board

class Game: # game class to handle game logic, color represents board color chosen by user
    def __init__(self, win, color):
        self.win = win
        self.color = color
        self.selected = None
        self.board = Main_Board(self.color)
        self.turn = RED
        self.valid_moves = {}
    
    def update(self): # update board to show current board
        self.board.draw(self.win)
        self.show_available_moves(self.valid_moves)
        pygame.display.update()

    def winner(self): # if winner has been found, return winner
        return self.board.winner()

    def select(self, row, col): # select piece to move and as a result show available moves
        if self.selected:
            result = self.move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        try:# this try catch must be here when user click outside board
            piece = self.board.get_piece(row, col)
            if piece != 0 and piece.color == self.turn:
                self.selected = piece
                self.valid_moves = self.board.get_valid_moves(piece)
                return True
        except:
            print("click_On_BOard")
        return False

    def move(self, row, col): # move piece to new position
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False

        return True

    def show_available_moves(self, moves): # show available moves for selected piece
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, YELLOW, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)

    def change_turn(self): # change turn to other player/color
        self.valid_moves = {}
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED

    def get_board(self): # return current board
        return self.board

    def ai_move(self, board): # move AI piece
        self.board = board
        self.change_turn()