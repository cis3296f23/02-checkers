"""
SecondMenu.py
The SecondMenu file and class powers the second menu of the game, which allows the user to choose between playing against another player or against the computer.
The class also creates an object of the game class to create the game the users plays.
"""
import pygame
from Player import Player
from Player import user_scores
from ScoreManager import ScoreManager
from constants import RED, SQUARE_SIZE, WHITE
from game import Game
from computer import minimax
from MusicClass import BackgroundMusic
from SharedObjects import background_music
from ThirdMenu import ThirdMenu



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

class SecondMenu:
    """
    The SecondMenu class consists of a String color, which represents the color of the board chosen by the user.
    The class also has three functions, start_game_menu, start_game_vs_player, and start_game_vs_computer.
    """

    def __init__(self, track):
        self.selected_music_track = track
        self.background_music = BackgroundMusic([track])

    color = RED
    def start_game_menu(self):
        """
        The start game menu function displays the second menu of the game, which allows the user to choose between playing against another player or against the computer.
        """


        global player1_name, player2_name
        start_game_screen = pygame.display.set_mode([Width, Height])

        message = "Select Game Mode"
        credits1 = "Developed by Wander Cerda-Torres, Barry Lin,"
        credits2 = "Nathan McCourt, Jonathan Stanczak, and Geonhee Yu"
        credits_font = pygame.font.Font(None, 25)

        # Credits text
        credits_text1 = credits_font.render(credits1, True, (255, 255, 255))
        credits_rect1 = credits_text1.get_rect(center=(Width // 2, 650))
        credits_text2 = credits_font.render(credits2, True, (255, 255, 255))
        credits_rect2 = credits_text2.get_rect(center=(Width // 2, 670))

        background_image = pygame.image.load("checkers.jpg")
        background_image = pygame.transform.scale(background_image, (Width, Height))

        title_font = pygame.font.Font(None, 64)
        title_text = title_font.render(message, True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(Width // 2, 38))

        # image of the background
        start_game_screen.blit(background_image, (0, 0))
        # display title information and credits
        start_game_screen.blit(title_text, title_rect)
        start_game_screen.blit(credits_text1, credits_rect1)
        start_game_screen.blit(credits_text2, credits_rect2)

        icon_size = (45, 45)  # Adjust the size of the icon as needed
        button_height = 50
        spacing = 10
        color = (128, 128, 128)  # grey

        # PvP Button
        position = (Width // 2 - 150, Height // 3 - 25)
        size = (300, 50)  # width, height

        button_font = pygame.font.Font(None, 32)
        button_text1 = button_font.render("Start Game VS Player", True, (255, 255, 255))  # Button text and color
        button_text_rect1 = button_text1.get_rect(center=(Width // 2, Height // 3))

        # Create button on screen using position and size parameters
        pygame.draw.rect(start_game_screen, color, pygame.Rect(position, size))
        start_game_screen.blit(button_text1, button_text_rect1)
        button_rect = pygame.Rect(position, size)

        # PvC Button
        position = (Width // 2 - 150, Height // 3 + button_height + spacing)
        size = (300, button_height)  # width, height

        button_text2 = button_font.render("Start Game VS Computer", True, (255, 255, 255))  # Button text and color
        button_text_rect2 = button_text2.get_rect(
            center=(Width // 2, Height // 3 + button_height + spacing + button_height // 2))

        # Create button on screen using position and size parameters
        pygame.draw.rect(start_game_screen, color, pygame.Rect(position, size))
        start_game_screen.blit(button_text2, button_text_rect2)
        button_rect_2 = pygame.Rect(position, size)

        # Exit Second Menu Button
        position = (Width // 2-150, Height // 3 + 135)
        size = (300, 50)  # width, height

        button_font = pygame.font.Font(None, 32)
        button_text3 = button_font.render("Back to Main Menu", True, (255, 255, 255)) # Button text and color
        button_text_rect3 = button_text3.get_rect(center=(Width // 2, Height // 3+160))
        pygame.draw.rect(start_game_screen, color, pygame.Rect(position, size))
        start_game_screen.blit(button_text3, button_text_rect3)

        pygame.draw.rect(start_game_screen, color, pygame.Rect(position, size))
        start_game_screen.blit(button_text3, button_text_rect3)
        button_rect_3 = pygame.Rect(position, size)

        pygame.display.flip()
        mouse = pygame.mouse.get_pos()

        while True:
            mouse = pygame.mouse.get_pos()
            if button_rect_3.collidepoint(mouse):

                pygame.draw.rect(start_game_screen, cursor_color, button_rect_3) # Change color when cursor hovered over
                start_game_screen.blit(button_text3, button_text_rect3)
                pygame.display.update()
            elif button_rect_2.collidepoint(mouse):

                pygame.draw.rect(start_game_screen, cursor_color, button_rect_2)
                start_game_screen.blit(button_text2, button_text_rect2)
                pygame.display.update()

            elif button_rect.collidepoint(mouse):
                pygame.draw.rect(start_game_screen, cursor_color, button_rect)
                start_game_screen.blit(button_text1, button_text_rect1)
                pygame.display.update()

            else:
                pygame.display.update()
                pygame.draw.rect(start_game_screen, color, button_rect_3) # stay original color if cursor not hovering over
                start_game_screen.blit(button_text3, button_text_rect3)

                pygame.draw.rect(start_game_screen, color, button_rect_2)
                start_game_screen.blit(button_text2, button_text_rect2)

                pygame.draw.rect(start_game_screen, color, button_rect)
                start_game_screen.blit(button_text1, button_text_rect1)

                pygame.display.update()


            for event in pygame.event.get():
                score_manager.load_scores()

                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if button_rect_3.collidepoint(event.pos):  # if exit button is clicked
                        return  # exit start game menu and return to menu
                    elif button_rect.collidepoint(event.pos):  # Start Game VS Player button clicked
                        player1_name.get_player_name()
                        score_manager.add_user(player1_name.username)
                        player2_name.get_player_name()
                        score_manager.add_user(player2_name.username)
                        self.start_game_vs_player(start_game_screen)
                        score_manager.save_scores()
                        return
                    elif button_rect_2.collidepoint(event.pos):  # Start Game VS Computer button clicked
                        player1_name.get_player_name()
                        score_manager.add_user(player1_name.username)
                        # Create an instance of ThirdMenu and start the difficulty menu
                        third_menu = ThirdMenu(self.selected_music_track, self.color,player1_name)  # Pass color too
                        third_menu.start_difficulty_menu()  # This will display the difficulty selection menu

                        return

                    elif event.type == self.background_music.SONG_END:
                        self.background_music.handle_event(event)

    def start_game_vs_player(self, screen):
        """
        The start game vs player function starts the game against another player by creating an object of the game class and passing the screen, color, and player names.
        """
        run = True
        clock = pygame.time.Clock()
        game = Game(screen, self.color, player1_name.username, player2_name.username)
        global score_manager, user_scores

        post_duration = 10000  # Display time in milliseconds
        post_text = None
        post_display_time = 0  # Initialize the time when the tweet is displayed

        while run:
            clock.tick(60)
            if game.winner() != None:
                print(game.winner())
                run = False
                if game.winner() == CHERRY:
                    player1_name.update_win()
                    score_manager.update_scores(player1_name)
                    player2_name.update_loss()
                    score_manager.update_scores(player2_name)
                elif game.winner() == WHITE:
                    player2_name.update_win()
                    score_manager.update_scores(player2_name)
                    player1_name.update_loss()
                    score_manager.update_scores(player1_name)

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
                        reddit_post = game.fetch_reddit_post()  # Fetch most recent Reddit post
                        if reddit_post:
                            post_text = reddit_post.title  # Store the post title
                            post_display_time = pygame.time.get_ticks() + post_duration  # Set the display time

                    else:
                        row, col = get_row_col_from_mouse(pos)
                        game.select(row, col)
                    # Check for background music event
                if event.type == background_music.SONG_END:
                    background_music.handle_event(event)

            game.update()
            # Display the fetched Reddit post
            if post_text and pygame.time.get_ticks() < post_display_time:
                game.display_text_box()  # Call the function to display the post
            else:
                post_text = None  # Clear the post when time is up

    pygame.display.flip()  # Update the display after drawing everything

