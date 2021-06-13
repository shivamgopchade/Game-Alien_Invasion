class Settings:
    def __init__(self):
        #screen
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(230,230,230)

        #ship speed
        self.ship_speed_factor=0.5
        self.ship_limit=3

        #bullet
        self.bullet_speed_factor=5
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=(60,60,60)
        self.bullets_allowed=3

        #alien
        self.alien_speed_factor=1
        self.fleet_drop_speed=10
        self.fleet_direction=1