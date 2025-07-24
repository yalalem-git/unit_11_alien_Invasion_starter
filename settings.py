
from pathlib import Path

class Settings:
    def __init__(self):
        self.name = "Alien Invasion"
        base_dir = Path(__file__).parent

        self.screen_width = 1200
        self.screen_height = 800
        self.FPS = 60

        self.starting_ship_count = 3 # New

        self.bg_file = base_dir / 'Assets' / 'images' / 'Starbasesnow.png'
        self.ship_file = base_dir / 'Assets' / 'images' / 'ship2(no bg).png'
        self.ship_w = 40
        self.ship_h = 60
        self.ship_speed = 5
        self.ship_side = "left"

        self.bullet_file = base_dir / 'Assets' / 'images' / 'laserBlast.png'
        self.laser_sound = base_dir / 'Assets' / 'sound' / 'laser.mp3'
        self.impact_sound = base_dir / 'Assets' / 'sound' / 'impactSound.mp3'

        self.bullet_speed = 7
        self.bullet_w = 25
        self.bullet_h = 80
        self.bullets_allowed = 1000  # note: used this name for consistency

        self.alien_file = base_dir / 'Assets' / 'images' / 'enemy_4.png'
        self.alien_w = 40
        self.alien_h = 40
        self.fleet_speed = 5
        self.fleet_drop_speed = 1
        self.fleet_direction = 1           # horizontal movement not used here but kept
        self.vertical_direction = 1        # 1 means moving down, -1 moving up
