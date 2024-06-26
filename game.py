# Simple pygame program

# Import and initalize the pygame libary
import pygame
from settings import Settings
from button import Button
from player import Player
from bubble import Bubble
from scoreboard import Scoreboard
from game_stats import GameStats
import game_functions as gf

def run_game():
    pygame.init()
    gm_settings = Settings()

    # Set up the drawing window
    screen = pygame.display.set_mode([gm_settings.screen_width, gm_settings.screen_height])
    pygame.display.set_caption(gm_settings.caption)

    # Set up Play button
    play_button = Button(gm_settings, screen, "Play")
    
    # Set up game score
    stats = GameStats()
    
    # Set up scoreboard
    sb = Scoreboard(gm_settings, screen, stats)
    
    # Set up clock on decent frame rate
    clock = pygame.time.Clock()
    
    # Instantiate player
    player = Player(screen)
    
    # Create groups to hold bubbles
    bubbles = pygame.sprite.Group()
    
   
   # Run until the user asks to quit
    while True:
        gf.check_events(gm_settings, screen, player, bubbles, stats, play_button)
        if stats.game_active:
            player.update()
            gf.update_bubbles(player, bubbles, stats, sb, gm_settings)
            bubbles.update()
        else:
            bubbles.empty()
        gf.update_screen(gm_settings, screen, player, bubbles, clock, stats, play_button, sb)
run_game()