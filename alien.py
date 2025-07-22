import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING
if TYPE_CHECKING:
      from alien_invasion import AlienInvasion


class Alien(Sprite):
      def __init__(self, game: 'AlienInvasion', x: float, y: float) -> None:
            super().__init__()


            self.screen = game.screen
            self.boundaries = game.screen.get_rect()
            self.settings = game.settings
            
            self.image = pygame.image.load(self.settings.alien_file)
            self.image = pygame.transform.scale(self.image, 
                              (self.settings.alien_w, self.settings.alien_h)
                              )

            self.image = pygame.transform.flip(self.image, True, False) 
            self.rect = self.image.get_rect()
            
           # self.rect.x = x  # Positioning based on the screen
            #self.rect.y = y 
            # Positioining the alien from the right vertical axis
            self.rect.x = self.boundaries.right - self.rect.width


            self.x = float(self.rect.x) 
            self.y = float(self.rect.y)
            # self.rect.centery = game.ship.rect.centery -- changed  

      
      def update(self) -> None:
          temp_speed = self.settings.fleet_speed
             #self.x -= self.settings.fleet_speed
             #self.rect.x = self.x
          temp_speed = self.settings.fleet_speed
          '''if self.moving_up and self.rect.top > self.boundaries.top:
                self.y -= temp_speed
          if self.moving_down and self.rect.bottom < self.boundaries.bottom:'''
          self.y += temp_speed 
          self.rect.y = self.y



      def draw_alien(self) -> None:
            self.screen.blit(self.image, self.rect)

      
