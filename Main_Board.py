import pygame
from constants import BLACK, WHITE

ROWS = 8
SQUARE_SIZE = 87

class MAIN_Board:
    def __init__(self, color1, color2, board_color):
        self.color1 = color1
        self.color2 = color2
        self.board_color = board_color

    def draw_squares(self, win):
        """
        Draw alternating black and white squares on the board.
        """
        win.fill(self.board_color)

        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, WHITE, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

            for col in range((row + 1) % 2, ROWS, 2):
                pygame.draw.rect(win, BLACK, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

