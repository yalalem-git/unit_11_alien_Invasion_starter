
import pygame
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from alien_fleet import AlienFleet

class Alien(pygame.sprite.Sprite):
    def __init__(self, fleet: "AlienFleet", x: float, y: float) -> None:
        super().__init__()
        self.fleet = fleet
        self.game = fleet.game
        self.settings = self.game.settings
        self.screen = self.game.screen
        
        self.image = pygame.image.load(str(self.settings.alien_file))
        self.image = pygame.transform.scale(self.image, (self.settings.alien_w, self.settings.alien_h))
        self.rect = self.image.get_rect()

        #self.y = float(self.rect.y)

       # self.x = float(x)
        #self.y = float(y)
        self.rect.x = x
        self.rect.y = y
        self.x = float(self.rect.x)     # ← new: track horizontal
        self.y = float(self.rect.y)

    def update(self):
       """Move the alien vertically based on fleet direction."""
       self.y += self.fleet.settings.vertical_direction * self.settings.fleet_speed
       self.rect.y = int(self.y)

    def draw_alien(self) -> None:
        self.screen.blit(self.image, self.rect)

    def check_edges(self) -> bool:
         #if alien touches top or bottom edges of the screen
        if self.rect.top <= 0 or self.rect.bottom >= self.settings.screen_height:
            return True
        return False

      