
 
"""
Program Name: Alien Invasion
Author: Yalalem Tegenie
A 2D side-scrolling shooter game built using Pygame. The player controls a ship that moves vertically
along the left edge of the screen and shoots horizontally to destroy waves of advancing aliens. 
The game ends if an alien collides with the ship or reaches the left side of the screen.

23 July 2025
"""
import sys
import pygame
from settings import Settings
from ship import Ship
from game_stats import GameStats
from arsenal import Arsenal
from alien_fleet import AlienFleet
from time import sleep
from buttons import Buttons
from hud import HUD

class AlienInvasion:
    """Main class to manage game behavior, state, and rendering for Alien Invasion"""
    def __init__(self) -> None:
        """Initialize the game, settings, screen, sound, ship, aliens, and HUD"""
        pygame.init()
        self.settings = Settings()
        self.settings.initialize_dynamic_settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(self.settings.name)
        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg, 
                (self.settings.screen_width, self.settings.screen_height))
        self.game_stats = GameStats(self) 
        self.HUD = HUD(self)
        self.running = True
        self.clock = pygame.time.Clock()
        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(str(self.settings.laser_sound))
        self.laser_sound.set_volume(0.7)
        self.impact_sound = pygame.mixer.Sound(str(self.settings.impact_sound))
        self.impact_sound.set_volume(0.7) 
        self.ship = Ship(self, Arsenal(self))
        self.alien_fleet = AlienFleet(self)
        self.alien_fleet.create_fleet()
        self.play_button = Buttons(self, 'Play')
        self.game_active = False
        self.ship.rect.x = 0
        self.ship.rect.y = self.settings.screen_height // 2

    def run_game(self):
        """Main game loop: process events, update state, and render screen each frame"""
        while self.running:
            self._check_events()
            if self.game_active:
                self.ship.update()
                self.alien_fleet.update_fleet()
                self._check_collisions()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _check_collisions(self) -> None:
        """Check for collisions between ship and aliens, bullets and aliens, and edge conditions"""
        if self.ship.check_collisions(self.alien_fleet.fleet):
            self._check_game_status()
        if self.alien_fleet.check_left_edge():
            self.restart_game()
        if self.ship.check_collisions(self.alien_fleet.fleet):
            self.restart_game()
        collisions = self.alien_fleet.check_collisions(self.ship.arsenal.bullets)
        if collisions:
            self.impact_sound.play()
            self.impact_sound.fadeout(500)
            self.game_stats.update(collisions) 
            self.HUD.update_scores()
        if self.alien_fleet.check_destroyed_status():
            self._reset_level()
            self.settings.increase_difficulty()
            self.game_stats.update_level()

    def _check_game_status (self)->None:
        """Check the ship's remaining lives and either reset level or end the game"""
        if self.game_stats.ship_left >= 0:
            self.game_stats.ship_left -= 1
            self._reset_level()
            sleep(0.5)
        else:
            self.game_active = False

    def _reset_level(self) -> None:
        """Clear bullets and aliens, and create a new alien fleet"""
        self.ship.arsenal.bullets.empty()
        self.alien_fleet.fleet.empty()
        self.alien_fleet.create_fleet()

    def restart_game(self)->None:
        """Reset all game state and settings to restart gameplay"""
        self.settings.initialize_dynamic_settings()
        self.game_stats.reset_stats()
        self.HUD.update_scores()
        self._reset_level
        self.ship._center_ship  
        self.game_active = True
        pygame.mouse.set_visible(False)

    def _update_screen(self) -> None:
        """Redraw all game elements and flip the display buffer"""
        self.screen.blit(self.bg, (0, 0))
        self.ship.draw()
        self.alien_fleet.draw()
        self.ship.arsenal.update_arsenal()
        self.ship.arsenal.draw()
        self.HUD.draw()

        if not self.game_active:
            self.play_button.draw()
            pygame.mouse.set_visible(True)
        pygame.display.flip()

    def _check_events(self):
        """Respond to keyboard, mouse, and quit events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.game_stats.init_saved_scores()
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and self.game_active == True:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_button_clicked()

    def _check_button_clicked(self):
        """Check if the Play button was clicked and restart the game if so"""
        mouse_pos = pygame.mouse.get_pos()
        if self.play_button.check_clicked(mouse_pos):
            self.restart_game()

    def _check_keyup_events(self, event) -> None:
        """Handle key releases for ship movement."""
        if event.key == pygame.K_w:
            self.ship.moving_up = False
        elif event.key == pygame.K_s:
            self.ship.moving_down = False

    def _check_keydown_events(self, event):
        """Handle key presses for movement, shooting, and quitting"""
        if event.key == pygame.K_w:
            self.ship.moving_up = True
        elif event.key == pygame.K_s:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            if self.ship.fire():
                self.laser_sound.play()
                self.laser_sound.fadeout(250)
        elif event.key == pygame.K_q:
            self.running = False
            self.game_stats.save_scores()
            pygame.quit()
            sys.exit()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()