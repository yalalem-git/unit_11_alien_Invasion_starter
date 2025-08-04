
import pygame
from alien import Alien
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class AlienFleet:
    """Manage a fleet of aliens including creation, movement, drawing, and collision detection."""

    def __init__(self, game: 'AlienInvasion'):
        """Initialize the AlienFleet with game context (Constructing)"""
        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()

    def create_fleet(self):
        """
        Create a fleet of aliens arranged in a vertical pattern starting at the center of the screen.
        The number of rows and columns is determined by screen space and alien size.
        """

        alien = Alien(self, 0, 0)
        alien_width, alien_height = alien.rect.size

        available_space_x = self.settings.screen_width // 2

        number_aliens_x = available_space_x // (2 * alien_width)

        available_space_y = (self.settings.screen_height - 3 * alien_height) // 2


        number_rows = available_space_y // (alien_height)

        for row in range(number_rows):
            for alien_number in range(number_aliens_x):
                x = self.settings.screen_width // 2 + alien_width + 2 * alien_width * alien_number
                y = alien_height + 2 * alien_height * row
                alien = Alien(self, x, y)
                self.fleet.add(alien)

    def update_fleet(self):
        """
        Update the position of all aliens in the fleet.
        If any alien hits the top or bottom edge, change the fleet's direction.
        """
        self.fleet.update()  
        if self._check_fleet_edges():
            self._change_fleet_direction()

    def _check_fleet_edges(self):
        """Return True if any alien hits top or bottom edge."""
        for alien in self.fleet:
            if alien.check_edges():
                return True
        return False

    def _change_fleet_direction(self):
        """
        Reverse the fleet's vertical movement direction and adjust alien positions slightly.
        """
        self.settings.vertical_direction *= -1
        for alien in self.fleet:
            alien.x -= self.settings.fleet_drop_speed
            alien.rect.x = int(alien.x)

    def check_left_edge(self):
        """Return True if any alien reaches left screen edge (where ship is)."""
        for alien in self.fleet:
            if alien.rect.left <= 0:
                return True
        return False

    def check_collisions(self, bullets):
        """Check collisions between aliens and the ship"""
        return pygame.sprite.groupcollide(self.fleet, bullets, True, True)

    def check_destroyed_status(self):
        """Check if all aliens in the fleet have been destroyed"""
        if not self.fleet:
            return True
        return False


    def draw(self):
        """Draw all aliens in the fleet to the screen"""
        for alien in self.fleet:
            alien.draw_alien()