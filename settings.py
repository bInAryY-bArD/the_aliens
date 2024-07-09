class Settings():
    #a class to store all the settings of alien_invasion
    
    def __init__(self):
        #initialise the game settings
        
        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        #ship settings
        self.ship_speed_factor = 1.5

        #bullet settings
        self.bullet_speed_factor = 0.75
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = 100, 100, 100
        self.bullets_allowed = 5
