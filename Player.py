"""
Player.py
The Player File holds the Player class which is responsible for managing the players. This file holds a global user scores hashmap.
"""

import pygame
Width, Height = 1000, 700
background_image = pygame.image.load("checkers.jpg")
background_image = pygame.transform.scale(background_image, (Width, Height))
screen = pygame.display.set_mode([Width, Height])

# Global map for user scores
user_scores = {}

class Player:
    """
    The Player class is responsible for managing the players, and contains functions to initialize a player, update the win and loss, and get the player name.
    """
    def __init__(self, username, score):
        """
        The init function initializes the player object with a username and score.
        """
        self.username = username
        self.score = 0
        self.win = 0
        self.difficulty = 2
        
    
    def draw_text_input(self, player_name, error_msg="name error"):
        """
        The draw text input function draws the text input box on the screen.
        """
        font = pygame.font.Font(None, 32)

        # Render the background box
        pygame.draw.rect(screen, (128, 128, 128), (Width // 2 - 225, Height // 2 - 25, 450, 50))  # Adjust size and position as needed

        # Render the text on the background box
        input_text = font.render("Enter Your Name: " + player_name, True, (255, 255, 255))
        input_rect = input_text.get_rect(center=(Width // 2, Height // 2))
        screen.blit(input_text, input_rect)

        # Render the error message below the input box
        if error_msg:
            error_font = pygame.font.Font(None, 24)
            error_text = error_font.render(error_msg, True, (255, 0, 0))  # Red color for error message
            error_rect = error_text.get_rect(center=(Width // 2, Height // 2 + 30))  # Adjust position as needed
            screen.blit(error_text, error_rect)


    def get_player_name(self):
        """
        The get player name function gets the player name from the user and returns the player name.
        """
        input_active = True
        player_name = ""
        error_msg = ""

        while input_active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        #if player_name.isalnum() and len(player_name) <= 20:
                        if (event.unicode.isalnum() or event.unicode.isspace()) and len(player_name) < 20:

                            input_active = False  # Stop taking input when Enter is pressed and the name is valid
                        else:
                            error_msg = "Invalid name. Please use English letters or numbers, and keep it under 20 characters."
                    elif event.key == pygame.K_BACKSPACE:
                        player_name = player_name[:-1]  # Remove the last character when Backspace is pressed
                    else:
                        # Check if the typed character is an English letter, a number, or a space
                        if (event.unicode.isalnum() or event.unicode.isspace()) and len(player_name) < 20:
                            player_name += event.unicode  # Append the typed character to the player_name



            screen.blit(background_image, (0, 0))
            self.draw_text_input(player_name, error_msg)
            pygame.display.flip()
            
        self.username = player_name

        return player_name
        
    def update_win(self):
        """
        The update win function updates the win for a player by setting the win attribute to one.
        """
        self.win = 1

    def update_loss(self):
        """
        The update loss function updates the loss for a player by setting the win attribute to zero.
        """
        self.win = 0