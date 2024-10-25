import pygame
from Player import Player
from Player import user_scores
from ScoreManager import ScoreManager
from constants import RED, SQUARE_SIZE, WHITE
from game import Game
from computer import minimax
from MusicClass import BackgroundMusic
from SharedObjects import background_music


# Define constants here
Width, Height = 1000, 700
background_image = pygame.image.load("checkers.jpg")
background_image = pygame.transform.scale(background_image, (Width, Height))
screen = pygame.display.set_mode([Width, Height])
pygame.init()

player1_name = Player("Player 1", 0)
player2_name = Player("Player 2", 0)
score_manager = ScoreManager("user_data/user_data.json")
cursor_color = (100, 100, 100) # darker grey
color = (128, 128, 128) # grey


def get_row_col_from_mouse(pos):
    """
    This function gets the row and column of the mouse position. This is necessary for selecting pieces in the class.
    """
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


class ThirdMenu:
    """
    The ThirdMenu class allows the user to choose the difficulty level for playing against the computer.
    """
    # Define time limits for each difficulty level
    TIME_LIMITS = {
        "Easy": 10,    # 10 seconds for Easy
        "Normal": 5,   # 5 seconds for Normal
        "Hard": 2      # 2 seconds for Hard
    }

    def __init__(self, track, color, player1_name):
        self.selected_music_track = track
        self.background_music = BackgroundMusic([track])
        self.player1_name = player1_name  # Store player1_name
        self.color = color
        self.difficulty = None  # Variable to store selected difficulty

    def set_difficulty(self, selected_difficulty):
        if selected_difficulty in ["Easy", "Normal", "Hard"]:
            self.difficulty = selected_difficulty
        else:
            self.difficulty = None

    def start_difficulty_menu(self):
        """
        The difficulty menu function displays options for selecting the difficulty level.
        """
        start_game_screen = pygame.display.set_mode([Width, Height])
        message = "Select Difficulty Level"
        title_font = pygame.font.Font(None, 64)
        title_text = title_font.render(message, True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(Width // 2, 50))

        button_font = pygame.font.Font(None, 32)
        cursor_color = (100, 100, 100)  # Darker grey
        color = (128, 128, 128)  # Grey


        # Difficulty Buttons
        difficulty_buttons = [
            ("Easy" , (Width // 2 - 150, Height // 3), (300, 50)),
            ("Normal" , (Width // 2 - 150, Height // 3 + 60), (300, 50)),
            ("Hard" , (Width // 2 - 150, Height // 3 + 120), (300, 50)),
        ]

        # Display the background
        background_image = pygame.image.load("checkers.jpg")
        background_image = pygame.transform.scale(background_image, (Width, Height))
        start_game_screen.blit(background_image, (0, 0))

        # Draw title
        start_game_screen.blit(title_text, title_rect)

        # Create and draw buttons
        button_rects = []
        for text , pos, size in difficulty_buttons:
            button_rect = pygame.Rect(pos, size)
            button_rects.append(button_rect)

            # Draw the button
            pygame.draw.rect(start_game_screen, color, button_rect)
            button_text = button_font.render(text, True, (255, 255, 255))
            text_rect = button_text.get_rect(center=button_rect.center)
            start_game_screen.blit(button_text, text_rect)

        pygame.display.flip()

        # Main loop for the difficulty menu
        while True:
            mouse = pygame.mouse.get_pos()

            for button_rect in button_rects:
                if button_rect.collidepoint(mouse):
                    pygame.draw.rect(start_game_screen, cursor_color, button_rect)
                else:
                    pygame.draw.rect(start_game_screen, color, button_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i, button_rect in enumerate(button_rects):
                        if button_rect.collidepoint(event.pos):
                            self.difficulty = ["Easy", "Normal", "Hard"][i]
                            print(f"Selected difficulty: {self.difficulty}")
                            # Start the game with the selected difficulty
                            self.start_game_vs_computer(start_game_screen, self.difficulty)
                            return  # Exit the menu after starting the game

        pygame.display.update()

    def start_game_vs_computer(self, screen, difficulty):
        """
        Starts the game against the computer with the selected difficulty level.
        """
        run = True
        clock = pygame.time.Clock()
        game = Game(screen, self.color, self.player1_name.username, "Computer")

        # Get time limit based on difficulty
        time_limit = self.TIME_LIMITS[difficulty]
        move_timer = time_limit
        last_move_time = pygame.time.get_ticks()  # Get current ticks

        # Define depth based on difficulty
        depth = 2  # Default depth
        if difficulty == "Easy":
            depth = 2
        elif difficulty == "Normal":
            depth = 4
        elif difficulty == "Hard":
            depth = 6


        while run:
            clock.tick(60)

            current_time = pygame.time.get_ticks()
            elapsed_time = (current_time - last_move_time) / 1000  # Convert to seconds
            move_timer -= elapsed_time
            last_move_time = current_time

            post_duration = 10000  # Display time in milliseconds
            post_text = None
            post_display_time = 0  # Initialize the time when the tweet is displayed

            # Check if time is up
            if move_timer <= 0:
                print("Time's up! You lose the turn.")
                game.change_turn()  # Hypothetical method to switch turns
                move_timer = time_limit  # Reset timer for the next turn

            if game.turn == WHITE:
                value, new_board = minimax(game.get_board(), depth, WHITE, game)
                game.ai_move(new_board)

            if game.winner() is not None:
                print(game.winner())
                run = False
                # Handle scoring here

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                #Feature to quit at any point of the game
                if event.type ==pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos() #if button is clicked
                    quit_button = game.display_quit()
                    if quit_button.collidepoint(pos):
                        run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    reddit_button = game.display_button()  # Draw button
                    if reddit_button.collidepoint(pos):  # If Reddit button clicked
                        print('Fetching Reddit post...')
                        reddit_post = game.fetch_reddit_post()  # Fetch most recent reddit post
                        if reddit_post:
                            post_text = reddit_post.title  # Store the post title
                            post_display_time = pygame.time.get_ticks() + post_duration  # Set the display time

                    else:
                        row, col = get_row_col_from_mouse(pos)
                        game.select(row, col)

            game.update()
            # Display the fetched Reddit post
            if post_text and pygame.time.get_ticks() < post_display_time:
                game.display_text_box()  # Call the function to display the post
            else:
                post_text = None  # Clear the post when time is up

    pygame.display.flip()  # Update the display after drawing everything

