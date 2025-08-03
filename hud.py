import pygame.font

from typing import TYPE_CHECKING

if TYPE_CHECKING:
      from alien_invasion import AlienInvasion

class HUD:


      def __init__(self, game: "AlienInvasion")->None:
            self.game = game
            self.settings = game.settings
            self.screen = game.screen
            self.boundaries = game.screen.get_rect()
            self.game_stats = game.game_stats
            self.font = pygame.font.Font(self.settings.font_file,
                                         self.settings.HUD_font_size)
            
            self.padding = 20
            self.update_scores()
           # self.setup_life_image()
           # self.update_level()

      def update_scores(self)->None:
          
          self._update_max_score()
          self._update_score()
          self._update_hi_score()
          self._setup_life_image()
          self.update_level()


      def _setup_life_image(self)->None:
            self.life_image = pygame.image.load(self.settings.ship_file)
            self.life_image = pygame.transform.scale(self.life_image, (
                  self.settings.ship_w, self.settings.ship_h
            ))

            self.life_image = pygame.transform.flip(self.life_image, True, False)
            self.life_image = pygame.transform.rotate(self.life_image, -90)

            self.life_rect = self.life_image.get_rect()
            

            
      def _update_score(self)-> None:
            score_str = f'SCORE: {self.game_stats.score:,.0f}'
            self.score_image = self.font.render(score_str, True,
                                                self.settings.text_color, None)
            
            self.score_rect = self.score_image.get_rect()
            #self.score_rect.top = self.boundaries.left - self.padding
            ##self.score_rect.left = self.boundaries.top + 40
            #self.score_rect.left = self.max_score_rect.bottom + self.padding
            ##self.score_rect.top = self.padding
             # Align right, near screen right edge with padding

            self.score_rect.right = self.boundaries.right - self.padding
              # Position below the score image with padding
            self.score_rect.top = self.score_rect.bottom + self.padding




                
      def _update_max_score(self)-> None:
            max_score_str = f'MAX_SCORE: {self.game_stats.max_score:,.0f}'
            self.max_score_image = self.font.render(max_score_str, True,
                                                self.settings.text_color, None)
            
            self.max_score_rect = self.max_score_image.get_rect()


           # self.max_score_rect.left = self.padding
           #self.max_score_rect.left = self.max_score_rect.bottom - self.padding
           # Align right same as score
            self.max_score_rect.right = self.boundaries.right - self.padding
            # Start near top with padding
            self.max_score_rect.top = self.padding




                  
      def _update_hi_score(self)-> None:
            hi_score_str = f'HI_SCORE: {self.game_stats.hi_score:,.0f}'
            self.hi_score_image = self.font.render(hi_score_str, True,
                                                self.settings.text_color, None)
            
            self.hi_score_rect = self.hi_score_image.get_rect()

            #self.hi_score_rect.left = self.padding
            #self.hi_score_rect.centery = self.boundaries.centery - 80

            # Align right same as others
            self.hi_score_rect.right = self.boundaries.right - self.padding
            # Vertically centered on screen:
            self.hi_score_rect.centery = self.boundaries.centery
            
      def update_level(self)-> None:
            level_str = f'LEVEL: {self.game_stats.level:,.0f}'
            self.level_image = self.font.render(level_str, True,
                                                self.settings.text_color, None)
            self.level_rect = self.level_image.get_rect()
            self.level_rect.right = self.boundaries.right - self.settings.ship_w - 2 * self.padding
            self.level_rect.bottom = self.boundaries.bottom - self.padding

      
      def _draw_lives(self) -> None:
         """Draw remaining lives at the bottom-right, stacked vertically upward."""
         image_width = self.life_rect.width
         image_height = self.life_rect.height
         total_lives = self.game_stats.ship_left

         current_x = self.boundaries.right - image_width - self.padding
         current_y = self.boundaries.bottom - image_height - self.padding

         for _ in range(total_lives):
             self.screen.blit(self.life_image, (current_x, current_y))
             current_y -= image_height + self.padding

      def draw(self)->None:
            self.screen.blit(self.hi_score_image, self.hi_score_rect)
            self.screen.blit(self.max_score_image, self.max_score_rect)
            self.screen.blit(self.score_image, self.score_rect)
            self.screen.blit(self.level_image, self.level_rect )
            self._draw_lives()


