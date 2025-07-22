'''import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING
if TYPE_CHECKING:
      from alien_fleet import AlienFleet


class Alien(Sprite):
      def __init__(self, fleet: 'AlienFleet', x: float, y: float) -> None:
            super().__init__()

            self.fleet = fleet
            self.screen = fleet.game.screen
            self.settings = fleet.game.settings
            self.boundaries = self.screen.get_rect()

            
            self.image = pygame.image.load(self.settings.alien_file)
            self.image = pygame.transform.scale(self.image, 
                              (self.settings.alien_w, self.settings.alien_h)
                              )
            self.image = pygame.transform.rotate(self.image, -90)

            #self.image = pygame.transform.flip(self.image, True, False) 
            self.rect = self.image.get_rect()
            self.rect.x = x  # Positioning based on the screen
            self.rect.y = y 
            # Positioining the alien from the right vertical axis
           # self.rect.x = self.boundaries.right - self.rect.width
           # self.rect.x = x  # Positioning based on the screen
            #self.rect.y = y 
# Positioining the alien from the right vertical axis
            self.rect.x = self.boundaries.right - self.rect.width


            self.x = float(self.rect.x) 
            self.y = float(self.rect.y)
            # self.rect.centery = game.ship.rect.centery -- changed  

      
      def update(self) -> None:
          temp_speed = self.settings.fleet_speed

          if self.check_edges():
                self.settings.fleet_direction *= -1
                self.x -= self.settings.fleet_drop_speed

        
          self.y += temp_speed  * self.settings.fleet_direction
          self.rect.x = self.x
          self.rect.y = int(self.y) # update y position for vertical movement


      def check_edges (self) -> bool:
            return (self.rect.top <= self.boundaries.top or self.rect.bottom >= self.boundaries.bottom)



      def draw_alien(self) -> None:
            self.screen.blit(self.image, self.rect)'''
import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from alien_fleet import AlienFleet

class Alien(Sprite):
    def __init__(self, fleet: 'AlienFleet', x: float, y: float) -> None:
        super().__init__()

        self.fleet = fleet
        self.screen = fleet.game.screen
        self.settings = fleet.game.settings
        self.boundaries = self.screen.get_rect()

        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(self.image, 
                        (self.settings.alien_w, self.settings.alien_h))
        #self.image = pygame.transform.flip(self.image, True, False)  # Face left
        self.image = pygame.transform.rotate(self.image, -90)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

       
    def update(self) -> None:
        # Move leftward constantly
        self.x -= self.settings.fleet_speed
        self.rect.x = int(self.x)

         # Move vertically, bouncing at top/bottom
        self.y += self.settings.vertical_direction * self.settings.fleet_speed
        self.rect.y = int(self.y)

    def check_edges(self) -> bool:
        return (
               self.rect.top <= self.boundaries.top or 
               self.rect.bottom >= self.boundaries.bottom
    )

    def draw_alien(self) -> None:
        self.screen.blit(self.image, self.rect)

      
