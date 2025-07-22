from pathlib import Path
class Settings:
    def __init__(self):
        self.name:str = "Alien Invasion"
        '''Path is not working for some reason so I use this'''
        base_dir = Path(__file__).parent
        self.screen_width = 1200
        self.screen_height = 800
        self.FPS = 60
        self.bg_file = base_dir / 'Assets'/'images'/'Starbasesnow.png'
        self.ship_file = base_dir /'Assets'/'images'/'ship2(no bg).png'
        self.ship_w = 40
        self.ship_h = 60
        self.ship_speed = 5
        self.bullet_file = base_dir / 'Assets' / 'images' / 'laserBlast.png'
        self.laser_sound = base_dir / 'Assets' / 'sound' / 'laser.mp3'
        self.bullet_speed = 7
        self.bullet_w = 25
        self. bullet_h = 80
        self.bullet_amount = 5        
        self.ship_side = "left"
        
       # self.alien_file = base_dir / 'Assets' / 'images' / 'alienenemy_4.png'
        #self.alien_w = 40
      #  self.alien_h = 40
       # self.fleet_speed = 5'''

        self.alien_file = base_dir / 'Assets' / 'images' / 'enemy_4.png'
        self.alien_w = 40
        self.alien_h = 40
        self.fleet_speed = 5
        self.fleet_direction = 1
        self.fleet_drop_speed = 1
        self.vertical_direction = 1
    


