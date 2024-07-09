import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    #a class to represent bullets

    def __init__(self, ai_settings, screen, ship):
        #create a bullet object at the ship's location
        super().__init__()
        self.screen = screen

        #create a bullet rect at (0,0) and
        # set the correct position
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #store the bullet's position in decimal value
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    #move the bullet up the screen
    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y

    #draw the bullet to the screen
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
