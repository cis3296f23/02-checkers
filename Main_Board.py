import pygame
from constants import BLACK, WHITE

ROWS = 8
SQUARE_SIZE = 50

class Board:
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

    def draw_piece(self, win, row_index, col_index, piece_color):
        """
        Draw a checker piece on the board.
        """
        radius = SQUARE_SIZE // 2 - 5
        center = (col_index * SQUARE_SIZE + SQUARE_SIZE // 2, row_index * SQUARE_SIZE + SQUARE_SIZE // 2)
        pygame.draw.circle(win, piece_color, center, radius)
