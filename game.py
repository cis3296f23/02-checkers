"""
Game.py
The game file holds the game logic and game class.
"""
import pygame
import requests
import random
import redditwarp.SYNC
from constants import RED, WHITE, YELLOW, SQUARE_SIZE, CHERRY
from Main_Board import Main_Board

class Game: 
    """
    The Game class is responsible for managing the game logic, and contains functions to initialize the game, check the turn timeout, display the turn,
    display the piece count, display the player names, update the board, check for a winner, select a piece, move a piece, show available moves, change the turn,
    get the board, and move an AI piece.
    """

    def __init__(self, win, color, player1, player2):
        """
        The init function initializes the Game class with a window, color, player1, and player2, and sets the turn start time and turn timeout. The text color is set to white,
        and the urgent text color is set to red. The screen is set to the window size, and the player names are set to player1 and player2.
        """
        self.turn_start_time = pygame.time.get_ticks()
        self.turn_timeout = 5200  # 5.2 seconds per turn
        self.win = win
        self.color = color
        self.selected = None
        self.board = Main_Board(self.color)
        self.turn = CHERRY
        self.valid_moves = {}
        self.font = pygame.font.Font(None, 36)  # Font for rendering text
        self.text_color = WHITE  # Text color
        self.text_urgent_color = RED  # Text color when time is running out
        self.screen = pygame.display.set_mode((1000, 700))
        self.player1 = player1
        self.player2 = player2
        self.post = None  # Initialize as None, or remove if not necessary
        self.post_time = 0  # Time when the Reddit post was fetched
        self.post_duration = 10 * 1000  # 10 seconds in milliseconds

    def fetch_reddit_post(self):
        client = redditwarp.SYNC.Client()
        m = next(client.p.subreddit.pull.top('Temple', amount=1, time='hour'))
        print(m.title)
        print(m.permalink)

    def display_text_box(self):
        """
            Displays a white box and the provided tweet text inside the box if available and within the display time.
        """
        box_rect = pygame.Rect(690, 400, 300, 300)  # Box dimensions
        pygame.draw.rect(self.screen, (255, 255, 255), box_rect)  # Draw white box

        # Check if the tweet should be displayed
        current_time = pygame.time.get_ticks()
        if self.post and current_time - self.post_time < self.post_duration:
            font = pygame.font.Font(None, 24)  # Smaller font for tweets
            lines = self.wrap_text(self.post, font, box_rect.width)

            # Display each line in the white box
            y_offset = 410  # Starting Y position
            for line in lines:
                post_surface = font.render(line, True, (0, 0, 0))  # Black text
                self.screen.blit(post_surface, (700, y_offset))
                y_offset += 30  # Line spacing
        else:
            self.post = ""  # Clear the tweet if time is up

    def wrap_text(self, text, font, max_width):
        """
        A helper function to wrap text to fit inside the box width.
        """
        words = text.split(' ')
        lines = []
        current_line = ""

        for word in words:
            # Test if adding the next word will exceed the width
            test_line = current_line + word + " "
            if font.size(test_line)[0] <= max_width:
                current_line = test_line
            else:
                # If the test line exceeds max width, add current line to lines and start a new one
                lines.append(current_line)
                current_line = word + " "

        # Add any remaining words as the last line
        if current_line:
            lines.append(current_line)

        return lines

    def draw_reddit_button(self):
        """
        Draws a button on the game screen to fetch tweets.
        """
        button_rect = pygame.Rect(730, 250, 200, 50)  # Button dimensions
        pygame.draw.rect(self.screen, (255, 128, 0), button_rect)  # Button color
        text_surface = self.font.render("Get Post", True, self.text_color)
        self.screen.blit(text_surface, (760, 265))  # Positioning the text in the button
        return button_rect

    def check_turn_timeout(self):
        """
        The check turn timeout function checks the turn timeout and displays the move timer on the screen. If the time is running out, the text color is set to red.
        """
        elapsed_time = pygame.time.get_ticks() - self.turn_start_time
        elapsed_seconds = elapsed_time // 1000 
        text = f"Move Timer: {elapsed_seconds} s"
        text_surface = self.font.render(text, True, self.text_color)
        if elapsed_time > 3000:
            text_surface = self.font.render(text, True, self.text_urgent_color)
        else:
            text_surface = self.font.render(text, True, self.text_color)
        # Render text
        self.screen.blit(text_surface, (715, 50))
        if elapsed_time > self.turn_timeout:
            self.change_turn()

    def display_turn(self):
        """
        The display turn function displays the current turn on the screen.
        """
        if self.turn == CHERRY:
            text = f"Current Turn: RED"
        else:
            text = f"Current Turn: WHITE"
        text_surface = self.font.render(text, True, self.text_color)
        self.screen.blit(text_surface, (715, 100))

    def display_piece_count(self): 
        """
        The display piece count function displays the piece count on the screen.
        """
        text = f"RED Pieces Left: {self.board.red_left}"
        text2 = f"WHITE Pieces Left: {self.board.white_left}"
        text_surface = self.font.render(text, True, self.text_color)
        text_surface2 = self.font.render(text2, True, self.text_color)
        self.screen.blit(text_surface, (715, 150))
        self.screen.blit(text_surface2, (715, 200))

    def display_button(self):
        """
        The display player names function displays the player names on the screen.
        """
        font = pygame.font.Font(None, 32)
        text_color = (255,255,255)
        button_rect = pygame.Rect(730, 250, 200, 50)  # Button dimensions
        pygame.draw.rect(self.screen, (0, 128, 255), button_rect)  # Button color
        text_surface = font.render("Get Tweet", True, text_color)
        self.screen.blit(text_surface, (770, 265)) # Positioning the text in the button
        return button_rect

    def display_player_names(self, player1, player2):
        """
        The display player names function displays the player names on the screen.
        """
        text = f"Player 1: {player1}"
        text2 = f"Player 2: {player2}"
        text_surface = self.font.render(text, True, self.text_color)
        text_surface2 = self.font.render(text2, True, self.text_color)
        self.screen.blit(text_surface, (715, 320))
        self.screen.blit(text_surface2, (715, 370))

    def update(self): 
        """
        The update function updates the board to show the current board and features.
        """
        self.board.draw(self.win)
        self.show_available_moves(self.valid_moves)
        self.check_turn_timeout()
        self.display_turn()
        self.display_piece_count()
        self.display_player_names(self.player1, self.player2)
        self.display_button()
        self.display_text_box()
        pygame.display.update()
        
    def winner(self): 
        """
        The winner function checks if a winner has been found by calling the board winner function and returns the winner if one has been found.
        """
        return self.board.winner()

    def select(self, row, col): 
        """
        The select function selects a piece and shows the available moves for the piece.
        """
        if self.selected:
            result = self.move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        
        try:
            piece = self.board.get_piece(row, col)
            if piece != 0 and piece.color == self.turn:
                self.selected = piece
                self.valid_moves = self.board.get_valid_moves(piece)
                return True
        except:
            return None
            
        return False

    def move(self, row, col):
        """
        The move function moves a piece to a given row and column and changes the turn.
        """
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

    def show_available_moves(self, moves): 
        """
        The show available moves function shows the available moves for the selected piece.
        """
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, YELLOW, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)

    def change_turn(self): 
        """
        The change turn function changes the turn to the other player/color and resets the turn timer.
        """
        self.valid_moves = {}
        self.turn_start_time = pygame.time.get_ticks()  # Reset the turn timer
        if self.turn == CHERRY:
            self.turn = WHITE
        else:
            self.turn = CHERRY

    def get_board(self): 
        """
        The get board function returns the current board.
        """
        return self.board

    def ai_move(self, board): 
        """
        The ai move function moves the AI piece in a player vs computer game.
        """
        self.board = board
        self.change_turn()