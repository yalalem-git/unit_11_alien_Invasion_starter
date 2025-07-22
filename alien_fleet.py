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
      self.fleet_direction = self.settings.fleet_direction
      self.drop_speed = self.settings.fleet_speed

      self.create_fleet()

   def create_fleet(self)-> None:
      alien_w = self.settings.alien_w
      alien_h = self.settings.alien_h
      screen_h = self.settings.screen_height
      screen_w = self.settings.screen_width

      fleet_w = self.calculate_fleet_size(alien_w, screen_h)

      fleet_vertical_space = fleet_w * alien_w
      y_offset = int((screen_h - fleet_vertical_space) // 2)

# some modifications to the fleet creat vertical screen fit
      cols = screen_w // (2 * alien_w )
      rows = screen_h // (2 * alien_h)

      for row in range(rows):
         for col in range(cols):
            x = alien_w + 2 * alien_w * col 
            y = alien_h + 2 * alien_h * row
            self._create_alien(x, y)

   def calculate_fleet_size(self, alien_w, screen_h):
       fleet_w = (screen_h//alien_w)

       if fleet_w  % 2 == 0:
           fleet_w -= 1
       else:
          fleet_w -= 2

       return fleet_w
   
   def _create_alien(self, current_x: int, current_y:int):
      new_alien = Alien(self, current_x, current_y)

      self.fleet.add(new_alien)

   def draw(self) ->None:
      alien: 'Alien'
      for alien in self.fleet:
         alien.draw_alien()