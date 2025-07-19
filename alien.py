import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING
if TYPE_CHECKING:
      from alien_invasion import AlienInvasion


class Bullets(Sprite):
      def __init__(self, game: 'AlienInvasion') -> None:
            super().__init__()
            self.screen = game.screen
            self.settings = game.settings
            
            self.image = pygame.image.load(self.settings.bullet_file)
            self.image = pygame.transform.scale(self.image, 
                              (self.settings.bullet_w, self.settings.bullet_h)
                              )

            '''self.rect =  self.image.get_rect()
            #self.rect.midtop = game.ship.rect.midtop
            self.y = float(self.rect.y)'''
            self.rect = self.image.get_rect()
            self.rect.centery = game.ship.rect.centery

            if game.ship.side == "left":
                self.rect.left = game.ship.rect.right
                self.direction = 1
            else:
                self.rect.right = game.ship.rect.left
                self.direction = -1
                self.image = pygame.transform.flip(self.image, True, False)  # Flip bullet to face left

            self.x = float(self.rect.x)
            self.y = float(self.rect.y)
      
      def update(self) -> None:
            self.x += self.direction * self.settings.bullet_speed
            self.rect.x = self.x

      def draw_bullet(self) -> None:
            self.screen.blit(self.image, self.rect)

      
