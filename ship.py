import pygame
from settings import Settings
class Ship:
      from alien_invasion import ALienInvassion
      def __init__(self, game:ALienInvassion):
            self.game = game
            self.settings = game.settings
            self.screen = game.screen
            self.screen_rect = self.screen.get_rect()
            self.image = game.image.load(self.settings.ship_file)
            self.image = game.image.transform.scale(self.image, (self.settings.ship_w, self.settings.ship_h))
            self.rect = self.image.get_rect()
            self.rect.midbottom = self.screen_rect.midbottom