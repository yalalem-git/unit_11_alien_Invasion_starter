import pygame
from alien import Alien

from typing import TYPE_CHECKING
from bullet import Bullets
if TYPE_CHECKING:
      from alien_invasion import AlienInvasion
class Arsenal:
    """Manage the player's bullets (arsenal), including firing, updating, and drawing them"""
    def __init__(self, game: 'AlienInvasion') -> None:
        """Initialize arsenal with reference to the game"""
        self.game = game
        self.settings = game.settings
        self.bullets = pygame.sprite.Group()

    def fire_bullet(self):
        """Fire a bullet if the allowed limit has not been reached"""
        if len(self.bullets) < self.settings.bullets_allowed:
            bullet = Bullets(self.game)
            self.bullets.add(bullet)
            return True
        return False

    def update_arsenal(self):
        """Update the positions of all bullets and remove those that go off-screen"""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.left > self.settings.screen_width:
                self.bullets.remove(bullet)

    def draw(self):
        """Draw all bullets in the arsenal onto the screen"""
        for bullet in self.bullets:
            bullet.draw_bullet()


