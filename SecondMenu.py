import pygame
from Player import Player
from Player import user_scores
from constants import RED, SQUARE_SIZE, WHITE
from game import Game
from computer import minimax

Width, Height = 1000, 700
background_image = pygame.image.load("checkers.jpg")
background_image = pygame.transform.scale(background_image, (Width, Height))
screen = pygame.display.set_mode([Width, Height])

player1_name = Player("Player 1")
player2_name = Player("Player 2")

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

class SecondMenu:
    
    #default board color if users do not choose a color
    color = RED
    
    def start_game_menu(self):
        global player1_name, player2_name
        pygame.init()
        
        start_game_screen = pygame.display.set_mode([Width, Height])
        pygame.display.set_caption("Start Game Menu")

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
        button_text = button_font.render("Start Game VS Player", True, (255, 255, 255))  # Button text and color
        button_text_rect = button_text.get_rect(center=(Width // 2, Height // 3))

        # Create button on screen using position and size parameters
        pygame.draw.rect(start_game_screen, color, pygame.Rect(position, size))
        start_game_screen.blit(button_text, button_text_rect)
        button_rect = pygame.Rect(position, size)

        # PvC Button
        position = (Width // 2 - 150, Height // 3 + button_height + spacing)
        size = (300, button_height)  # width, height

        button_text = button_font.render("Start Game VS Computer", True, (255, 255, 255))  # Button text and color
        button_text_rect = button_text.get_rect(
        center=(Width // 2, Height // 3 + button_height + spacing + button_height // 2))

        # Create button on screen using position and size parameters
        pygame.draw.rect(start_game_screen, color, pygame.Rect(position, size))
        start_game_screen.blit(button_text, button_text_rect)
        button_rect_2 = pygame.Rect(position, size)
        
        # Exit Second Menu Button
        position = (Width // 2-150, Height // 3 + 135)
        size = (300, 50)  # width, height

        button_font = pygame.font.Font(None, 32)
        button_text = button_font.render("Back to Main Menu", True, (255, 255, 255)) # Button text and color
        button_text_rect = button_text.get_rect(center=(Width // 2, Height // 3+160))
        pygame.draw.rect(start_game_screen, color, pygame.Rect(position, size))
        start_game_screen.blit(button_text, button_text_rect)

        pygame.draw.rect(start_game_screen, color, pygame.Rect(position, size))
        start_game_screen.blit(button_text, button_text_rect)
        button_rect_3 = pygame.Rect(position, size)

        pygame.display.flip()
        mouse = pygame.mouse.get_pos()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if button_rect_3.collidepoint(event.pos):  # if exit button is clicked
                        return  # exit start game  and return to menu
                    elif button_rect.collidepoint(event.pos):  # Start Game VS Player button clicked
                        player1_name.get_player_name()
                        player1_name.add_user(player1_name.username)
                        player2_name.get_player_name()
                        player2_name.add_user(player2_name.username)
                        self.start_game_vs_player(start_game_screen)
                    elif button_rect_2.collidepoint(event.pos):  # Start Game VS Computer button clicked
                        player1_name.get_player_name()
                        player1_name.add_user(player1_name.username)
                        self.start_game_vs_computer(start_game_screen)
                        
    def start_game_vs_player(self, screen): # start game against player
        run = True
        clock = pygame.time.Clock()
        game = Game(screen, self.color)

        # Exit Button
        button_font = pygame.font.Font(None, 32)
        exit_text = button_font.render("Exit Game", True, (255, 255, 255))
        exit_button_rect = exit_text.get_rect(center=(Width // 2+350, Height - 100))
        pygame.draw.rect(screen, (128, 128, 128), exit_button_rect)
        screen.blit(exit_text, exit_button_rect)
        pygame.display.flip()

        while run:
            clock.tick(60)
            if game.winner() != None:
                print(game.winner())
                run = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    row, col = get_row_col_from_mouse(pos)
                    game.select(row, col)

            game.update()

        self.start_game_menu()

    def start_game_vs_computer(self, screen): # start game vs computer minimax algorithm
        run = True
        clock = pygame.time.Clock()
        game = Game(screen, self.color)

        # Exit Button
        button_font = pygame.font.Font(None, 32)
        exit_text = button_font.render("Exit Game", True, (255, 255, 255))
        exit_button_rect = exit_text.get_rect(center=(Width // 2+350, Height - 100))
        pygame.draw.rect(screen, (128, 128, 128), exit_button_rect)
        screen.blit(exit_text, exit_button_rect)
        pygame.display.flip()

        while run:
            clock.tick(60)
            if game.turn == WHITE:
                # prints computer thinking once 
                print("TWOO_Computer is Thinking")
                value, new_board = minimax(game.get_board(), 4, WHITE, game)
                game.ai_move(new_board) 

            if game.winner() != None:
                print(game.winner())
                run = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    row, col = get_row_col_from_mouse(pos)
                    game.select(row, col)

            game.update()
    
        self.start_game_menu()
    

    # Display the player's name at the right bottom corner
    #player_name_font = pygame.font.Font(None, 24)
    #player_name_text = player_name_font.render(player1_name, True, (255, 255, 255))  # White text color
    #player_name_rect = player_name_text.get_rect(bottomright=(Width - 10, Height - 10))  # Adjust position as needed
    
    # Display player name in the right bottom corner
    #pygame.draw.rect(screen, (0, 0, 255), player_name_rect)  # Blue box
    #screen.blit(player_name_text, player_name_rect)
