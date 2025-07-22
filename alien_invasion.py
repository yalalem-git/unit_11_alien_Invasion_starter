"""
Alien Invasion

This game is a modified version of the classic Alien Invasion project, built using Pygame.
I have edited the game code from the classroom videos just to make the fire horizontal.

Author: Yalalem Tegenie

17 July 2025
"""


import sys
import pygame
from settings import Settings
from ship import Ship
from arsenal import Arsenal
from alien import Alien

class AlienInvasion:

    def __init__(self)-> None:

        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg, 
                (self.settings.screen_width, self.settings.screen_height))

        self.running = True
        self.clock = pygame.time.Clock()
    

        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(str(self.settings.laser_sound))
        self.laser_sound.set_volume(0.7)
               
        self.ship = Ship(self, Arsenal(self))
        self.alien = Alien(self, 10, 10)
          # EDIT 1: Position ship on left border, centered vertically
        self.ship.rect.x = 0
        self.ship.rect.y = self.settings.screen_height // 2


    
    def run_game (self):
        while self.running:
            self._check_events()

            self.ship.update()
            self.alien.update()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _update_screen(self)->None:
        self.screen.blit(self.bg, (0,0))
        self.ship.draw()
        self.alien.draw_alien()
        pygame.display.flip()

    
    def _check_events(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   self.running = False
                   pygame.quit()                    
                   sys.exit()
                elif event.type  == pygame.KEYDOWN:
                    self._check_keydown_events(event)

                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event) 

    def _check_keyup_events(self, event)->None:
       if event.key == pygame.K_w:
            self.ship.moving_up = False
       elif event.key == pygame.K_s:
            self.ship.moving_down = False
        
    def _check_keydown_events(self, event):
        if event.key == pygame.K_w: 
            self.ship.moving_up = True

        elif event.key == pygame.K_s:
            self.ship.moving_down = True


        elif event.key == pygame.K_SPACE:
            if self.ship.fire():
                #play the laser sound
                self.laser_sound.play()
                self.laser_sound.fadeout(250)

        elif event.key == pygame.K_q:
            self.running = False
            pygame.quit()
            sys.exit()

if __name__ == "__main__":
    """Test comment""" 
    ai = AlienInvasion()
    ai.run_game()
  
