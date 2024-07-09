import pygame
from pygame.sprite import Sprite


class Alien():
    #a class to represent alien
    
    def __init__(self, ai_settings, screen):

        #inititalize the alien and
        #its starting position
        self.screen = screen
        self.ai_settings = ai_settings

        #load the image and its rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.image = pygame.transform.scale(self.image, (60, 30))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #start each new alien at
        #top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store the alien's exact position
        self.x = float(self.rect.x)

    def blitme(self):
        #draw the alien at it's current position
        self.screen.blit(self.image, self.rect)