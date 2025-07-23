
import pygame
from typing import TYPE_CHECKING
if TYPE_CHECKING:
   from alien_invasion import AlienInvasion
from alien import Alien

class AlienFleet:
   
    def __init__(self, game: "AlienInvasion")-> None:
        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()
        self.settings.vertical_direction = 1  # 1 means down, -1 means up
        
        self.create_fleet()

    def create_fleet(self) -> None:
        alien_w = self.settings.alien_w
        alien_h = self.settings.alien_h
        screen_h = self.settings.screen_height
        screen_w = self.settings.screen_width

        # Limit fleet width to right half of screen
        fleet_h, fleet_w = self.calculate_fleet_size(alien_h, screen_h, alien_w, screen_w // 2)
        
        half_screen = screen_w // 2
        alien_spacing = 2 * alien_w

        fleet_vertical_space = fleet_h * alien_h
        fleet_horizontal_space = fleet_w * alien_spacing

        x_offset, y_offset = self.calculate_offset(half_screen, fleet_horizontal_space, fleet_vertical_space, screen_h)

        for row in range(fleet_h):
            for col in range(fleet_w):
                current_y = alien_h * row + y_offset
                current_x = half_screen + (alien_spacing * col) + x_offset
                self._create_alien(current_x, current_y)

    def calculate_fleet_size(self, alien_h, screen_h, alien_w, half_screen_w):
        fleet_h = screen_h // alien_h
        fleet_w = half_screen_w // int(alien_w * 1.5)

        if fleet_h % 2 == 0:
            fleet_h -= 1
        else:
            fleet_h -= 2

        if fleet_w % 2 == 0:
            fleet_w -= 1
        else:
            fleet_w -= 2

        return int(fleet_h), int(fleet_w)

    def calculate_offset(self, half_screen, fleet_horizontal_space, fleet_vertical_space, screen_h):
        x_offset = (half_screen // 2) - (fleet_horizontal_space // 2)
        y_offset = (screen_h - fleet_vertical_space) // 2
        return x_offset, y_offset

    def _create_alien(self, current_x: int, current_y: int) -> None:
        new_alien = Alien(self, current_x, current_y)
        self.fleet.add(new_alien)

    def _check_fleet_edges(self):
        for alien in self.fleet:
            if alien.check_edges():
                # Bounce vertical direction
                self.settings.vertical_direction *= -1
                
                # Move fleet left by 1 pixel on bounce
                for alien in self.fleet:
                    alien.x -= 1
                    alien.rect.x = int(alien.x)
                break

    def update_fleet(self) -> None:
        self._check_fleet_edges()
        self.fleet.update()

    def draw(self) -> None:
        for alien in self.fleet:
            alien.draw_alien()

    def check_collisions(self, other_group):
        collisions = pygame.sprite.groupcollide(self.fleet, other_group, True, True)

    
    def check_destroyed_status(self)->None:
        if not self.fleet:
            return True
        return False
    
    def check_destroyed_status(self):
        return self.fleet
        