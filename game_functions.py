import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_events(ai_settings, screen, ship, bullets):
    #respond to key presses and movements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ai_settings, screen, ship, bullets)
            

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    #respond to key down events
            
        if event.key == pygame.K_LEFT:
            #move the ship to the left
            ship.moving_left = True

        elif event.key == pygame.K_RIGHT:
            #move the ship to the right
            ship.moving_right = True

        elif event.key == pygame.K_SPACE:
            #fire a bullet
            fire_bullet(ai_settings, screen, ship, bullets)

        elif event.key == pygame.K_q:
             #press q to exit
             sys.exit()

def check_keyup_events(event, ai_settings, screen, ship, bullets):
     #respond to key up events
                
        if event.key == pygame.K_LEFT:
            #stop the left movement
            ship.moving_left = False

        elif event.key == pygame.K_RIGHT:
            #stop the right movement
            ship.moving_right = False
            
def update_screen(ai_settings, screen, ship, aliens, bullets):

    screen.fill(ai_settings.bg_color)

    #redraw all bulletsbehind ship and aliens
    for bullet in bullets:
         bullet.update()
         bullet.draw_bullet()

    #redraw the screen with each pass through loop
    ship.blitme()

    #redraw the alien with each pass through loop
    #alien.blitme()

    #draw the aliens
    aliens.draw(screen)
    
    #make the most recently drawn screen visible
    pygame.display.flip()

def update_bullets(bullets):
     #update pos of bullets and
     #get rid of old bullets

     #update bullets
     bullets.update

     #get rid of old bullets
     for bullet in bullets.copy():
          if bullet.rect.bottom <= 0:
               bullets.remove(bullet)

def fire_bullet(ai_settings, screen, ship, bullets):
    #limit the number of bullets
    if len(bullets) < ai_settings.bullets_allowed:
        #fireee
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def create_fleet(ai_settings, screen, aliens):
     #create a full row of aliens
     #find the number of aliens in a row
     #each alien has a spacing of 1 alien between them
     alien = Alien(ai_settings, screen)