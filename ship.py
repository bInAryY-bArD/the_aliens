import pygame

class Ship():

    def __init__(self, screen, ai_settings):
        #initialise ship and set its starting point
        self.screen = screen
        self.ai_settings = ai_settings
        
        #load the image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.image = pygame.transform.scale(self.image, (70,80))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #start each ship at the bottom-mid of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        #store a decimal value for the centre of the ship
        self.center = float(self.rect.centerx)
        
        #movement flags
        self.moving_left = False
        self.moving_right = False
        
    def update(self):
        #update the ship's movement based on the flag
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_settings.ship_speed_factor
            
        elif self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        #update rect object from self.center
        self.rect.centerx = self.center
        
    def blitme(self):
        #draw the ship at its current location
        self.screen.blit(self.image, self.rect)