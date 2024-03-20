# Simple pygame program

# Import and initalize the pygame libary
import pygame
from settings import Settings
<<<<<<< HEAD
=======
from player import Player
import game_functions as gf
>>>>>>> setup-game-window

def run_game():
    pygame.init()
    gm_settings = Settings()

<<<<<<< HEAD
    # Set up the drawing window
    screen = pygame.display.set_mode([gm_settings.screen_width, gm_settings.screen_height])
    pygame.display.set_caption(gm_settings.caption)

    # Run until user asks to quit
    running = True
    while running:
        screen.fill(gm_settings.big_color)
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Flip the display
        pygame.display.flip()
    # Done! Time to quit.    
    pygame.quit()
=======
    
    screen = pygame.display.set_mode([gm_settings.screen_width, gm_settings.screen_height])
    pygame.display.set_caption(gm_settings.caption)



    player = Player(screen)

    while True:
        gf.check_events(player)
        player.update()
        gf.update_screen(gm_settings, screen, player)
>>>>>>> setup-game-window

run_game()