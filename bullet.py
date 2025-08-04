
import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
class Bullets(Sprite):
    """
    Represents a bullet fired by the player's ship.
    The bullet travels horizontally based on the ship's side.
    Uses a custom image, rotation, scaling, and directional logic
    """
    def __init__(self, game: 'AlienInvasion') -> None:
        """Initialize the bullet at the ship's position and set its direction"""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.image = pygame.image.load(str(self.settings.bullet_file)).convert_alpha() 
        self.image = pygame.transform.rotate(self.image, -90) # new
        self.image = pygame.transform.scale(self.image, 
                          (self.settings.bullet_w, self.settings.bullet_h))
        self.rect = self.image.get_rect()
        self.rect.centery = game.ship.rect.centery
        if game.ship.side == "left":
            self.rect.left = game.ship.rect.right
            self.direction = 1
        else:
            self.rect.right = game.ship.rect.left
            self.direction = -1
            self.image = pygame.transform.flip(self.image, True, False)
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self) -> None:
        """Update the bullet's position based on its direction and speed"""
        self.x += self.direction * self.settings.bullet_speed
        self.rect.x = int(self.x)

    def draw_bullet(self) -> None:
        """Draw the bullet image onto the screen"""
        self.screen.blit(self.image, self.rect)