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
        self.bullet_amount = 100        
        self.ship_side = "left"
        self.ship_side = "right"