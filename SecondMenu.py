import pygame
from Main_Board import MAIN_Board
from constants import RED, GREY
from pieces import Piece


Width, Height = 1000, 700 

class SecondMenu:

    # default colors
    color1 = RED
    color2 = GREY

    def start_game_menu(self):
        pygame.init()

        start_game_screen = pygame.display.set_mode([Width, Height])
        pygame.display.set_caption("Start Game Menu")

        message = "Select Game Mode"
        credits1 = "Developed by Wander Cerda-Torres, Barry Lin,"
        credits2 = "Nathan McCourt, Jonathan Stanczak, and Geonhee Yu"
        credits_font = pygame.font.Font(None, 25)

        # Credits text
        credits_text1 = credits_font.render(credits1, True, (255, 255, 255))
        credits_rect1 = credits_text1.get_rect(center=(Width // 2, 940))
        credits_text2 = credits_font.render(credits2, True, (255, 255, 255))
        credits_rect2 = credits_text2.get_rect(center=(Width // 2, 960))

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
                        self.start_game_vs_player(start_game_screen)
                    elif button_rect_2.collidepoint(event.pos):  # Start Game VS Computer button clicked
                        self.start_game_vs_computer(start_game_screen)
                        
    

    def start_game_vs_player(self, screen):
        #main_Board changes piece color
        main_board = MAIN_Board(self.color2, self.color1, (0, 0, 0))
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill((0, 0, 0))
            
            # Draw the board and pieces
            main_board.draw_board(screen)
            main_board.draw_pieces(screen)

            pygame.display.flip()

        pygame.quit()

    def start_game_vs_computer(self, screen):
        #main_Board changes piece color
        main_board = MAIN_Board(self.color1, self.color2, (0, 0, 0))
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.fill((0, 0, 0))
            
            # Draw the board and pieces
            main_board.draw_board(screen)
            main_board.draw_pieces(screen)

            pygame.display.flip()

        pygame.quit()
