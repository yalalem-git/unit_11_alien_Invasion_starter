'''import pygame
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

      fleet_h, fleet_w = self.calculate_fleet_size(alien_h, screen_h, alien_w, screen_w)
      
      half_screen = self.settings.screen_width//2

      fleet_vertical_space = fleet_h * alien_h
      fleet_horizontal_space = fleet_w * alien_w

      y_offset = (screen_h - fleet_vertical_space) // 2
      x_offset = (half_screen - fleet_horizontal_space)//2


      for row in range(fleet_h):
         # = screen_w - (alien_w + 2 * alien_w * col) 
         for col in range(fleet_w):
            current_y = alien_h  * row + y_offset
           # current_x  = alien_w * col  + x_offset
            current_x = self.settings.screen_width - alien_w - (alien_w * 2 * col) - x_offset # my addition
         
            #int(y_offset + 2 * alien_h * row)  #screen_h - (alien_h + 2 * alien_h * row)  # making aliens center
           
            self._create_alien(current_x, current_y)


   def calculate_fleet_size(self, alien_h, screen_h, alien_w, screen_w):
       fleet_h = (screen_h//  alien_h)
       fleet_w = (screen_w//alien_w)

       if fleet_h  % 2 == 0:
           fleet_h -= 1
       else:
          fleet_h -= 2
       if fleet_w % 2 == 0:
          fleet_w -= 1
       else:
          fleet_w -= 2

       return int(fleet_h), int(fleet_w)
   
   def _create_alien(self, current_x: int, current_y:int)-> None:
      new_alien = Alien(self, current_x, current_y)

      self.fleet.add(new_alien)

   def draw(self) ->None:
      alien: 'Alien'
      for alien in self.fleet:
         alien.draw_alien()'''
import pygame
from typing import TYPE_CHECKING
if TYPE_CHECKING:
   from alien_invasion import AlienInvasion

from alien import Alien

class AlienFleet:

    def __init__(self, game: "AlienInvasion") -> None:
        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = self.settings.fleet_direction
        self.drop_speed = self.settings.fleet_speed

        self.create_fleet()

    def create_fleet(self) -> None:
        alien_w = self.settings.alien_w
        alien_h = self.settings.alien_h
        screen_w = self.settings.screen_width
        screen_h = self.settings.screen_height

        # Half of screen reserved for fleet
        fleet_area_w = screen_w // 2
        fleet_area_h = screen_h

        # Calculate horizontal and vertical capacity
        aliens_per_row = fleet_area_w // (2 * alien_w)
        rows = fleet_area_h // (2 * alien_h)

        for row in range(rows):
            for col in range(aliens_per_row):
                current_x = screen_w - ((col + 1) * 2 * alien_w)
                current_y = alien_h + row * 2 * alien_h
                self._create_alien(current_x, current_y)

    def _create_alien(self, current_x: int, current_y: int) -> None:
        alien = Alien(self, current_x, current_y)
        self.fleet.add(alien)

    def draw(self) -> None:
        for alien in self.fleet:
            alien.draw_alien()