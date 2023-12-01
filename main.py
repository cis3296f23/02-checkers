# main.py
# holds menu operations for the game including sound, settings, leaderboard, tutorial, and board customization

import pygame
from SecondMenu import SecondMenu
from constants import BLUE, YELLOW, RED, GREEN
from ScoreManager import ScoreManager

pygame.init()
pygame.mixer.init() # initialize pygame mixer for music

# set up the drawing window
Width, Height = 1000, 700 # updated size
screen = pygame.display.set_mode([Width, Height])
#title of the game for screen 
pygame.display.set_caption("Checkers+")

# background music
tracks = ["music/Track1.mp3", "music/Track2.mp3", "music/Track3.mp3", "music/Track4.mp3"] # can add more or delete tracks if we do not like them
current_track = 0
SONG_END = pygame.USEREVENT + 1
def music_loop():
    global current_track
    pygame.mixer.music.load(tracks[current_track])
    pygame.mixer.music.set_volume(0.1) # 0.1-1.0, can change accordingly
    pygame.mixer.music.play()
    current_track = (current_track + 1) % len(tracks)

music_loop()
pygame.mixer.music.set_endevent(SONG_END) # create event for song ending/looping
music_playing = True # boolean to check if music is playing or not

# title for display (can remove credits if we do not want them)
game_title = "Checkers+"
message = "Checkers with a twist! For all ages and skill levels!"
credits1 = "Developed by Wander Cerda-Torres, Barry Lin,"
credits2 = "Nathan McCourt, Jonathan Stanczak, and Geonhee Yu"
background_image = pygame.image.load("checkers.jpg")
background_image = pygame.transform.scale(background_image, (Width, Height))  
title_font = pygame.font.Font(None, 64)
message_font = pygame.font.Font(None, 32)
credits_font = pygame.font.Font(None, 25)

# Title text
title_text = title_font.render(game_title, True, (255, 255, 255))
title_rect = title_text.get_rect(center=(Width // 2, 22))
# Under title text
message_text = message_font.render(message, True, (255, 255, 255))
message_rect = message_text.get_rect(center=(Width // 2, 55))
# Credits text
credits_text1 = credits_font.render(credits1, True, (255, 255, 255))
credits_rect1 = credits_text1.get_rect(center=(Width // 2, 650))
credits_text2 = credits_font.render(credits2, True, (255, 255, 255))
credits_rect2 = credits_text2.get_rect(center=(Width // 2, 670))

second_menu_instance = SecondMenu()

# run until the user closes application
def main():
    running = True
    while running:
        # did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                buttons = menu_buttons() # create array for buttons # NEED TO ADD PVC BUTTON OR MAKE PVP BUTTON COMBINED INTO BOTH
                if buttons[0].collidepoint(event.pos): # If Start Game button is clicked, show the second menu
                   second_menu_instance.start_game_menu()
                if buttons[2].collidepoint(event.pos): # if mouse is clicked on tutorial button
                    tutorial()
                elif buttons[1].collidepoint(event.pos): # if mouse is clicked on settings button
                    settings()
                elif buttons[4].collidepoint(event.pos): # if mouse is clicked on leaderboard button (not yet implemented)
                    board_customization()
                # Check if the current song has finished, loop to next song
            elif event.type == SONG_END:
                music_loop()

        #image of the background
        screen.blit(background_image, (0, 0))
        # display title information and credits
        screen.blit(title_text, title_rect)
        screen.blit(message_text, message_rect)
        screen.blit(credits_text1, credits_rect1)
        screen.blit(credits_text2, credits_rect2)
        
        # call PvP button function from menu.py
        menu_buttons()
        pygame.display.flip()

    # done! time to quit
    pygame.quit()

def menu_buttons(): # function to create menu buttons

    # Used for buttons w/ images
    icon_size = (45, 45)  # Adjust the size of the icon as needed
    button_height = 50
    spacing = 10

    # Start Game Button
    startgame_icon = pygame.image.load('pics/start_icon.png')
    # Draw the icon next to the text with the specified size
    startgame_icon_resized = pygame.transform.scale(startgame_icon, icon_size)
    startgame_icon_rect = startgame_icon_resized.get_rect(topleft=(Width // 2 - 150 + 10, Height // 3 + (button_height - icon_size[1] - 50) // 2))

    color = (128, 128, 128) # grey
    cursor_color = (100, 100, 100) # darker grey
    position = (Width // 2-150, Height // 3-25)
    size = (300, 50)  # width, height
        
    button_font = pygame.font.Font(None, 32)
    button_text = button_font.render("Start Game", True, (255, 255, 255)) # Button text and color
    button_text_rect = button_text.get_rect(center=(Width // 2, Height // 3))
    
    # Create button on screen using position and size parameters
    pygame.draw.rect(screen, color, pygame.Rect(position, size))
    screen.blit(startgame_icon_resized, startgame_icon_rect.topleft)
    screen.blit(button_text, button_text_rect)
    
    # Used to indicate if cursor is hovering over button. If so, button will be darker
    mouse = pygame.mouse.get_pos()
    button_rect = pygame.Rect(position, size)
    if button_rect.collidepoint(mouse):
        pygame.draw.rect(screen, cursor_color, button_rect)  # Change color when cursor hovered over
    else:
        pygame.draw.rect(screen, color, button_rect) # stay original color if cursor not hovering over

    screen.blit(button_text, button_text_rect)
    screen.blit(startgame_icon_resized, startgame_icon_rect.topleft)  # Draw the icon after drawing the button

    # Settings Button    
    settings_icon = pygame.image.load('pics/settings_icon.png')

    position = (Width // 2 - 150, Height // 3 + button_height + spacing)
    size = (300, button_height)  # width, height

    button_text = button_font.render("Settings", True, (255, 255, 255))  # Button text and color
    button_text_rect = button_text.get_rect(center=(Width // 2, Height // 3 + button_height + spacing + button_height // 2))

    # Draw the icon next to the text with the specified size
    settings_icon_resized = pygame.transform.scale(settings_icon, icon_size)
    settings_icon_rect = settings_icon_resized.get_rect(topleft=(Width // 2 - 150 + 10, Height // 3 + button_height + spacing + (button_height - icon_size[1]) // 2))

    # Create button on screen using position and size parameters
    pygame.draw.rect(screen, color, pygame.Rect(position, size))
    screen.blit(settings_icon_resized, settings_icon_rect.topleft)  # Draw the icon after drawing the button
    screen.blit(button_text, button_text_rect)

    # Used to indicate if the cursor is hovering over the button. If so, the button will be darker
    mouse = pygame.mouse.get_pos()
    button_rect_2 = pygame.Rect(position, size)
    if button_rect_2.collidepoint(mouse):
        pygame.draw.rect(screen, cursor_color, button_rect_2)  # Change color when cursor hovered over
    else:
        pygame.draw.rect(screen, color, button_rect_2)  # Stay the original color if the cursor is not hovering over

    screen.blit(settings_icon_resized, settings_icon_rect.topleft)  # Draw the icon after drawing the button
    screen.blit(button_text, button_text_rect)

    # Tutorial button
    tutorial_icon = pygame.image.load('pics/tutorial_icon.png')

    color = (128, 128, 128) # grey
    cursor_color = (100, 100, 100) # darker grey
    position = (Width // 2-150, Height // 3 + 135)
    size = (300, 50)  # width, height

    button_font = pygame.font.Font(None, 32)
    button_text = button_font.render("Tutorial", True, (255, 255, 255)) # Button text and color
    button_text_rect = button_text.get_rect(center=(Width // 2, Height // 3+160))
    pygame.draw.rect(screen, color, pygame.Rect(position, size))
    screen.blit(button_text, button_text_rect)

    # Draw the icon next to the text with the specified size
    tutorial_icon_resized = pygame.transform.scale(tutorial_icon, icon_size)
    tutorial_icon_rect = tutorial_icon_resized.get_rect(topleft=(Width // 2 - 150 + 10, Height // 3 + 135 + (button_height - icon_size[1]) // 2))

    pygame.draw.rect(screen, color, pygame.Rect(position, size))
    screen.blit(button_text, button_text_rect)
    
    # Used to indicate if cursor is hovering over button. If so, button will be darker
    mouse = pygame.mouse.get_pos()
    button_rect_3 = pygame.Rect(position, size)
    if button_rect_3.collidepoint(mouse):
        pygame.draw.rect(screen, cursor_color, button_rect_3)  # Change color when cursor hovered over
    else:
        pygame.draw.rect(screen, color, button_rect_3) # stay original color if cursor not hovering over

    screen.blit(tutorial_icon_resized, tutorial_icon_rect.topleft)  # Draw the icon after drawing the button
    screen.blit(button_text, button_text_rect)
    
    # Leaderboard button
    leaderboard_icon = pygame.image.load('pics/leaderboard_icon.png')

    color = (128, 128, 128) # grey
    cursor_color = (100, 100, 100) # darker grey
    position = (Width // 2 - 150, Height // 3 + 200)  # Adjust the vertical position as needed
    size = (300, 50)  # width, height

    button_font = pygame.font.Font(None, 32)
    button_text = button_font.render("View Rankings", True, (255, 255, 255)) # Button text and color
    button_text_rect = button_text.get_rect(center=(Width // 2, Height // 3 + 225))  # Adjust the vertical position as needed
    pygame.draw.rect(screen, color, pygame.Rect(position, size))
    screen.blit(button_text, button_text_rect)

    # Draw the icon next to the text with the specified size
    leaderboard_icon_resized = pygame.transform.scale(leaderboard_icon, icon_size)
    leaderboard_icon_rect = leaderboard_icon_resized.get_rect(
    topleft=(Width // 2 - 150 + 10, Height // 3 + 200 + (button_height - icon_size[1]) // 2))

    pygame.draw.rect(screen, color, pygame.Rect(position, size))
    screen.blit(button_text, button_text_rect)
    
    # Used to indicate if cursor is hovering over button. If so, button will be darker
    mouse = pygame.mouse.get_pos()
    button_rect_4 = pygame.Rect(position, size)
    if button_rect_4.collidepoint(mouse):
        pygame.draw.rect(screen, cursor_color, button_rect_4)  # Change color when cursor hovered over
        if pygame.mouse.get_pressed()[0]:  # Check if left mouse button is clicked
            show_leaderboard()  # Call the function to display the leaderboard
    else:
        pygame.draw.rect(screen, color, button_rect_4) # stay original color if cursor not hovering over

    screen.blit(leaderboard_icon_resized, leaderboard_icon_rect.topleft)  # Draw the icon after drawing the button
    screen.blit(button_text, button_text_rect)

    # Customize Piece button
    board_icon = pygame.image.load('pics/colorwheel_icon.png')

    color = (128, 128, 128) # grey
    cursor_color = (100, 100, 100) # darker grey
    position = (Width // 2 - 150, Height // 3 + 285)  # Adjust the vertical position as needed
    size = (300, 50)  # width, height

    button_font = pygame.font.Font(None, 32)
    button_text = button_font.render("Customize Pieces", True, (255, 255, 255)) # Button text and color
    button_text_rect = button_text.get_rect(center=(Width // 2, Height // 3 + 310))  # Adjust the vertical position as needed
    pygame.draw.rect(screen, color, pygame.Rect(position, size))
    screen.blit(button_text, button_text_rect)

    # Draw the icon next to the text with the specified size
    board_icon_resized = pygame.transform.scale(board_icon, icon_size)
    board_icon_rect = board_icon_resized.get_rect(topleft=(Width // 2 - 150 + 10, Height // 3 + 285 + (button_height - icon_size[1]) // 2))

    pygame.draw.rect(screen, color, pygame.Rect(position, size))
    screen.blit(button_text, button_text_rect)
    
    # Used to indicate if cursor is hovering over button. If so, button will be darker
    mouse = pygame.mouse.get_pos()
    button_rect_5 = pygame.Rect(position, size)
    if button_rect_5.collidepoint(mouse):
        pygame.draw.rect(screen, cursor_color, button_rect_5)  # Change color when cursor hovered over
    else:
        pygame.draw.rect(screen, color, button_rect_5) # stay original color if cursor not hovering over

    screen.blit(board_icon_resized, board_icon_rect.topleft)  # Draw the icon after drawing the button
    screen.blit(button_text, button_text_rect)

    return button_rect, button_rect_2, button_rect_3, button_rect_4, button_rect_5

def tutorial(): # tutorial prompt
    # load image used in tutorial
    checkers_icon = pygame.image.load('pics/checkersguy_icon.png')
    tutorial_screen = pygame.display.set_mode([Width, Height])
    tutorial_screen.fill((128, 128, 128))

    # First message
    tutorial_font = pygame.font.Font(None, 64)
    tutorial_text = tutorial_font.render("Welcome to Checkers+!", True, (255, 255, 255))
    tutorial_rect = tutorial_text.get_rect(center=(Width // 2, 50))
    tutorial_screen.blit(tutorial_text, tutorial_rect)

    # Second message
    tutorial_font = pygame.font.Font(None, 32)
    tutorial_text = tutorial_font.render("This tutorial should provide you with instructions on how to play and use Checkers+.", True, (255, 255, 255))
    tutorial_rect = tutorial_text.get_rect(center=(Width // 2, 105))
    tutorial_screen.blit(tutorial_text, tutorial_rect)

    # First paragraph
    tutorial_font = pygame.font.Font(None, 25)
    tutorial_text = tutorial_font.render("There are many features accessible from the Checkers+ main menu. You can start a PvP (player versus player) game,", True, (255, 255, 255))
    tutorial_rect = tutorial_text.get_rect(center=(Width // 2, 145))
    tutorial_screen.blit(tutorial_text, tutorial_rect)
    tutorial_text = tutorial_font.render("a PvC (player versus computer) game, and access other features like the settings, leaderboard, and this tutorial!", True, (255, 255, 255))
    tutorial_rect = tutorial_text.get_rect(center=(Width // 2, 170))
    tutorial_screen.blit(tutorial_text, tutorial_rect)
    tutorial_text = tutorial_font.render("The settings will allow you to turn music on or off, and customize the checkers board to your liking.", True, (255, 255, 255))
    tutorial_rect = tutorial_text.get_rect(center=(Width // 2, 195))
    tutorial_screen.blit(tutorial_text, tutorial_rect)
    tutorial_text = tutorial_font.render("The leaderboard will show recent match results, displaying who won and loss.", True, (255, 255, 255))
    tutorial_rect = tutorial_text.get_rect(center=(Width // 2, 220))
    tutorial_screen.blit(tutorial_text, tutorial_rect)

    # Create icon
    icon_size = (100, 100)
    button_height = 50
    spacing = 10
    checkers_icon_resized = pygame.transform.scale(checkers_icon, icon_size)
    checkers_icon_rect = checkers_icon_resized.get_rect(topleft=(Width // 2 - 150 + 95, Height // 3+30 + (button_height - icon_size[1]) // 2))
    screen.blit(checkers_icon_resized, checkers_icon_rect.topleft) 

    # Second paragraph
    tutorial_text = tutorial_font.render("To play Checkers+, standard checkers rules are applied...with a twist!", True, (255, 255, 255))
    tutorial_rect = tutorial_text.get_rect(center=(Width // 2, 365))
    tutorial_screen.blit(tutorial_text, tutorial_rect)
    tutorial_text = tutorial_font.render("In standard checkers, players can only move a piece diagonally until that piece has reached the last row", True, (255, 255, 255))
    tutorial_rect = tutorial_text.get_rect(center=(Width // 2, 390))
    tutorial_screen.blit(tutorial_text, tutorial_rect)
    tutorial_text = tutorial_font.render("of the opposing side. In our game, you will be allowed to move a piece backwards every 45 seconds, even", True, (255, 255, 255))
    tutorial_rect = tutorial_text.get_rect(center=(Width // 2, 415))
    tutorial_screen.blit(tutorial_text, tutorial_rect)
    tutorial_text = tutorial_font.render("if that piece has not yet reached the last row. You also only have 15 seconds to make a move, so think fast!", True, (255, 255, 255))
    tutorial_rect = tutorial_text.get_rect(center=(Width // 2, 440))
    tutorial_screen.blit(tutorial_text, tutorial_rect)
    tutorial_text = tutorial_font.render("Your 45 second timer will not reset until you make a backward move. Don't let them go to waste!", True, (255, 255, 255))
    tutorial_rect = tutorial_text.get_rect(center=(Width // 2, 465))
    tutorial_screen.blit(tutorial_text, tutorial_rect)
    tutorial_text = tutorial_font.render("When the game starts, you will be asked to enter the names of the players (or player, if playing against the computer).", True, (255, 255, 255))
    tutorial_rect = tutorial_text.get_rect(center=(Width // 2, 490))
    tutorial_screen.blit(tutorial_text, tutorial_rect)
    tutorial_text = tutorial_font.render("Doing this will allow your name(s) and score to be updated on the leaderboard.", True, (255, 255, 255))
    tutorial_rect = tutorial_text.get_rect(center=(Width // 2, 515))
    tutorial_screen.blit(tutorial_text, tutorial_rect)
    tutorial_text = tutorial_font.render("By now, you should have a basic understanding of what Checkers+ has to offer. Go give it a try!", True, (255, 255, 255))
    tutorial_rect = tutorial_text.get_rect(center=(Width // 2, 540))
    tutorial_screen.blit(tutorial_text, tutorial_rect)
    tutorial_text = tutorial_font.render("If you ever need to view this tutorial again, you can access it from the main menu. Have fun!", True, (255, 255, 255))
    tutorial_rect = tutorial_text.get_rect(center=(Width // 2, 565))
    tutorial_screen.blit(tutorial_text, tutorial_rect)

    # Exit button to return back to menu
    exit_button_font = pygame.font.Font(None, 32)
    exit_button_text = exit_button_font.render("Exit Tutorial", True, (255, 255, 255))
    exit_button_rect = exit_button_text.get_rect(center=(Width // 2, Height - 50))
    pygame.draw.rect(tutorial_screen, (64, 64, 64), exit_button_rect.inflate(20, 10))
    tutorial_screen.blit(exit_button_text, exit_button_rect)

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button_rect.collidepoint(event.pos):  # if exit tutorial button is clicked
                    return  # exit tutorial and return to menu
                
def settings(): # settings menu
    # Used for buttons w/ images
    icon_size = (45, 45)  # Adjust the size of the icon as needed
    button_height = 50
    spacing = 10
    settings_screen = pygame.display.set_mode([Width, Height])
    screen.blit(background_image, (0, 0))
    settings_screen.blit(title_text, title_rect)
    settings_screen.blit(message_text, message_rect)
    settings_screen.blit(credits_text1, credits_rect1)
    settings_screen.blit(credits_text2, credits_rect2)

    color = (128, 128, 128) # grey
    cursor_color = (100, 100, 100) # darker grey
    position = (Width // 2-150, Height // 3-25)
    size = (300, 50)  # width, height
    button_font = pygame.font.Font(None, 32)

    # Music Button
    music_icon = pygame.image.load('pics/music_icon.png')
    position = (Width // 2 - 150, Height // 3 + button_height + spacing)
    size = (300, button_height)  # width, height
    button_text = button_font.render("Music (On/Off)", True, (255, 255, 255))  # Button text and color
    button_text_rect = button_text.get_rect(center=(Width // 2, Height // 3 + button_height + spacing + button_height // 2))
    # Draw the icon next to the text with the specified size
    music_icon_resized = pygame.transform.scale(music_icon, icon_size)
    music_icon_rect = music_icon_resized.get_rect(topleft=(Width // 2 - 150 + 10, Height // 3 + button_height + spacing + (button_height - icon_size[1]) // 2))
    # Create button on screen using position and size parameters
    pygame.draw.rect(settings_screen, color, pygame.Rect(position, size))
    settings_screen.blit(music_icon_resized, music_icon_rect.topleft)  # Draw the icon after drawing the button
    settings_screen.blit(button_text, button_text_rect)
    button_rect_5 = pygame.Rect(position, size)

    # Exit button to return back to menu
    exit_button_font = pygame.font.Font(None, 32)
    exit_button_text = exit_button_font.render("Exit Settings", True, (255, 255, 255))
    exit_button_rect = exit_button_text.get_rect(center=(Width // 2, Height - 100))
    pygame.draw.rect(settings_screen, (128, 128, 128), exit_button_rect.inflate(20, 10))
    settings_screen.blit(exit_button_text, exit_button_rect)

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button_rect.collidepoint(event.pos):  # if exit settings button is clicked
                    return  # exit settings and return to menu
                if button_rect_5.collidepoint(event.pos):  # if music button is clicked
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.stop()  # Stop the music
                        music_playing = False
                    else:
                        music_loop()  # Start the music from next song in tracklist
                        music_playing = True

def show_leaderboard():
    # Set up the new window for the leaderboard
    leaderboard_screen = pygame.display.set_mode((1000, 700))
    pygame.display.set_caption("Leaderboard")
    screen.fill((128, 128, 128))
    # Leaderboard header
    header_font = pygame.font.Font(None, 36)
    header_text = header_font.render("Leaderboard", True, (255, 255, 255))
    header_rect = header_text.get_rect(center=(500, 40))
    leaderboard_screen.blit(header_text, header_rect)
    
    score_manager = ScoreManager("user_data/user_data.json")
    # Load scores from the JSON file
    score_manager.load_scores()

    # Sort players based on their scores in descending order
    sorted_players = sorted(score_manager.user_scores.items(), key=lambda x: x[1], reverse=True)

    # Extract the top ten players or all players if less than ten
    top_ten_players = sorted_players[:10]

    leaderboard_font = pygame.font.Font(None, 45)
    leaderboard_y = 80  # Adjust the vertical position as needed

    # Display the leaderboard in the new window
    for i, (username, score) in enumerate(top_ten_players):
        leaderboard_text = leaderboard_font.render(f"{i + 1}. {username}: {score} points", True, (255, 255, 255))
        leaderboard_text_rect = leaderboard_text.get_rect(center=(200, leaderboard_y + i * 30))
        leaderboard_text_rect.center = (500, leaderboard_y + i * 30)  # Adjust the horizontal position as needed
        leaderboard_screen.blit(leaderboard_text, leaderboard_text_rect)
        
    pygame.display.flip()

    # Exit button to return back to menu
    exit_button_font = pygame.font.Font(None, 32)
    exit_button_text = exit_button_font.render("Return to Main Menu", True, (255, 255, 255))
    exit_button_rect = exit_button_text.get_rect(center=(Width // 2, Height - 50))
    pygame.draw.rect(screen, (64, 64, 64), exit_button_rect.inflate(20, 10))
    screen.blit(exit_button_text, exit_button_rect)

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button_rect.collidepoint(event.pos):  # if exit tutorial button is clicked
                    return  # exit tutorial and return to menu

def board_customization(): # board customization menu, allows user to change color of board to either red, blue, yellow, or green
    board_customization_screen = pygame.display.set_mode([Width, Height])
    background_image = pygame.image.load("checkers.jpg")
    background_image = pygame.transform.scale(background_image, (Width, Height))
    # image of the background
    board_customization_screen.blit(background_image, (0, 0))
    board_customization_screen.blit(title_text, title_rect)
    board_customization_screen.blit(message_text, message_rect)
    board_customization_screen.blit(credits_text1, credits_rect1)
    board_customization_screen.blit(credits_text2, credits_rect2)
    # Exit button to return back to menu
    exit_button_font = pygame.font.Font(None, 32)
    exit_button_text = exit_button_font.render("Exit Board Customization", True, (255, 255, 255))
    exit_button_rect = exit_button_text.get_rect(center=(Width // 2, Height - 100))
    pygame.draw.rect(board_customization_screen, (128, 128, 128), exit_button_rect.inflate(20, 10))
    board_customization_screen.blit(exit_button_text, exit_button_rect)

    # Board Color Text
    board_color_font = pygame.font.Font(None, 32)
    board_color_text = board_color_font.render("Board Color", True, (255, 255, 255))
    text_rect = board_color_text.get_rect(center=(Width // 2 - 200, Height // 3 + 80))
    # Enlarge the box behind the text
    box_width = text_rect.width + 40  # Increase width
    box_height = text_rect.height + 20  # Increase height
    box_rect = pygame.Rect(text_rect.left - 20, text_rect.top - 10, box_width, box_height)
    # Draw the enlarged box behind the text
    pygame.draw.rect(board_customization_screen, (128, 128, 128), box_rect)
    board_customization_screen.blit(board_color_text, text_rect)
        
    square_side = 50  # Size of the square
    red_square_rect = pygame.Rect(text_rect.right + 50, text_rect.centery - square_side // 2, square_side, square_side)
    pygame.draw.rect(board_customization_screen, RED, red_square_rect)  # Red square
    blue_square_rect = pygame.Rect(red_square_rect.right + 20, red_square_rect.top, square_side, square_side)
    pygame.draw.rect(board_customization_screen, BLUE, blue_square_rect)  # Blue square
    yellow_square_rect = pygame.Rect(blue_square_rect.right + 20, blue_square_rect.top, square_side, square_side)
    pygame.draw.rect(board_customization_screen, YELLOW, yellow_square_rect)  # Yellow square
    green_square_rect = pygame.Rect(yellow_square_rect.right + 20, yellow_square_rect.top, square_side, square_side)
    pygame.draw.rect(board_customization_screen, GREEN, green_square_rect)  # Green square

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button_rect.collidepoint(event.pos):  # if exit settings button is clicked
                    return
                if red_square_rect.collidepoint(event.pos): # make board red
                    second_menu_instance.color = RED
                if blue_square_rect.collidepoint(event.pos): # make board blue
                    second_menu_instance.color = BLUE
                if yellow_square_rect.collidepoint(event.pos): # make board yellow
                    second_menu_instance.color = YELLOW
                if green_square_rect.collidepoint(event.pos): # make board green
                    second_menu_instance.color = GREEN

main()