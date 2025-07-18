import pygame
from settings import Settings
from typing import TYPE_CHECKING
if TYPE_CHECKING:
      from alien_invasion import AlienInvasion
      from arsenal import Arsenal

class Ship:
      
      def __init__(self, game: 'AlienInvasion', arsenal: 'Arsenal')-> None:
            self.game = game
            self.settings = game.settings
            self.screen = game.screen
            self.boundaries = self.screen.get_rect()

            self.image = pygame.image.load(self.settings.ship_file)

           
# Resize first
            self.image = pygame.transform.scale(
            self.image, (self.settings.ship_w, self.settings.ship_h)
        )

# Rotate 90° to face center (right if on left side, left if on right side)
            if self.settings.ship_side == "left":
                self.image = pygame.transform.rotate(self.image, -90)  # Face right
            else:
               self.image = pygame.transform.rotate(self.image, 90)   # Face left    
           
            self.side = game.settings.ship_side  # ← used to determine left or right side
            self.rect = self.image.get_rect()

        # Position the ship based on side
            if self.side == "left":
                self.rect.left = 0
            else:
                self.rect.right = self.boundaries.right
                self.image = pygame.transform.flip(self.image, True, False)  # face center

            self.rect.centery = self.boundaries.centery

            self.moving_up = False
            self.moving_down = False
            self.y = float(self.rect.y)
            self.arsenal = arsenal
      def update (self):
            # updating position of the ship
          self._update_ship_movement()
          self.arsenal.update_arsenal()


      def _update_ship_movement(self):
          temp_speed = self.settings.ship_speed
          if self.moving_up and self.rect.top > self.boundaries.top:
                self.y -= temp_speed
          if self.moving_down and self.rect.bottom < self.boundaries.bottom:
                self.y += temp_speed 
          self.rect.y = self.y

      def draw(self)-> None:
            self.arsenal.draw()
            self.screen.blit(self.image, self.rect)


      def fire(self)-> bool:
            return self.arsenal.fire_bullet()