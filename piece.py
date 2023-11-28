# holds code for piece class
import pygame
from constants import BLACK, WHITE, RED, BLUE, GREY, GREEN, PURPLE, ORANGE, SQUARE_SIZE, KING, ROWS, COLS

# reference from https://github.com/techwithtim/Python-Checkers

class Piece:
    padding = 15
    outline = 2
    
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        self.king = True   

    def draw(self, win):
        radius = SQUARE_SIZE // 2 - self.padding
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.outline)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.king:
            win.blit(KING, (self.x - KING.get_width() // 2, self.y - KING.get_height() // 2))
    
    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):
        return str(self.color)