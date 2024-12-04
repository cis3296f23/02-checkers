"""
Constants.py
The constants file holds the constants used in the game.
"""

import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
CHERRY = (183,33,70)
RED = (255, 0, 0)
GREY = (128,128,128)
GREEN = (0,128,0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ROWS, COLS = 8, 8
SQUARE_SIZE = 85
WIDTH, HEIGHT = 1000,1000

KING = pygame.transform.scale(pygame.image.load('pics/king_icon.png'), (44, 25)) # for king piece