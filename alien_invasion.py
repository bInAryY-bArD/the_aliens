import pygame

from settings import Settings
from ship import Ship
import game_functions
from bullet import Bullet
from pygame.sprite import Group
from alien import Alien

def run_game():
    #initialize game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    #make a ship
    ship = Ship(screen, ai_settings)

    #make a group to store bullets in
    bullets = Group()

    #make an alien
    aliens = Group()

    #create the fleet of aliens
    game_functions.create_fleet(ai_settings, screen, aliens)

    #start the main loop for the game
    while True:
        #watch for keyboard and mouse movements
        game_functions.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        game_functions.update_bullets(bullets)
        game_functions.update_screen(ai_settings, screen, ship, aliens, bullets)
        
run_game()
