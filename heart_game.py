import sys
from random import random

import pygame

from player import Player
from settings import Settings
from flags import Flags
from game_stats import GameStats
from ghosts import Ghosts

# create a menu by changing the game state
game_state = 0


class HeartGame:
    """Create a main heart game"""

    def __init__(self):
        """Initialize the game"""

        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Heart Game")
        score_value = 0
        font = pygame.font.Font(None, 32)
        textX = 10
        textY = 10

        # self.show_score(textX, textY)

        self.stats = GameStats(self)

        self.player = Player(self)
        self.flags = pygame.sprite.Group()
        self.ghosts = pygame.sprite.Group()

    def run_game(self):
        """Start the main loop to run the game"""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.player.update()
                self.create_flags()
                self._update_flags()
                self.create_ghosts()
                self._update_ghosts()

            self._update_screen()

    def show_score(x, y):
        """Show the score"""
        score = font.render("Score : " + str(score_value), True, (255, 255, 255))
        self.screen.blit(score, (x, y))
    def _check_events(self):
        """Respond to events such as keypresses and mouse"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keydown events"""
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_LEFT:
            self.player.moving_left = True
        elif event.key == pygame.K_RIGHT:
            self.player.moving_right = True
        elif event.key == pygame.K_a:
            self.player.moving_left = True
        elif event.key == pygame.K_d:
            self.player.moving_right = True
        elif event.key == pygame.K_SPACE:
            sys.exit()
            # this will be the pause screen?

    def _check_keyup_events(self, event):
        """Respond to keyup events"""
        if event.key == pygame.K_RIGHT:
            self.player.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.player.moving_left = False
        elif event.key == pygame.K_d:
            self.player.moving_right = False
        elif event.key == pygame.K_a:
            self.player.moving_left = False

    def create_flags(self):
        """Create flags that will fall down the screen"""
        if random() < self.settings.flag_appear:
            flag = Flags(self)
            self.flags.add(flag)

    def _update_flags(self):
        """Update flags on the screen"""
        self.flags.update()
        # check for flag and heart collision
        if pygame.sprite.spritecollideany(self.player, self.flags):
            self._player_hit()
        self._check_flag_edge()
    def _check_flag_edge(self):
        """Check if flag is off the edge"""
        for flag in self.flags.sprites():
            if flag.rect.bottom < 0:
                # Just want the flags to go off the screen, no bad stuff
                break
    def create_ghosts(self):
        """Create ghosts that will fall down the screen"""
        if random() < self.settings.ghost_appear:
            ghost = Ghosts(self)
            self.ghosts.add(ghost)

    def _update_ghosts(self):
        """Update ghosts on the screen"""
        self.ghosts.update()
        # check for ghost and heart collision
        if pygame.sprite.spritecollideany(self.player, self.ghosts):
            self._player_hit()
    def _player_hit(self):
        """Respond to getting hit by falling objects"""
        if self.stats.hearts_left > 0:
            self.stats.hearts_left -= 1
            # add the image of the hearts in the top left corner

            # restart the screen?
            self.flags.empty()
            self.ghosts.empty()
            self.player.center_heart()
        else:
            self.stats.game_active = False

    def _update_screen(self):
        """Update images on the screen"""
        self.screen.fill(self.settings.bg_color)
        self.player.blitme()

        self.flags.draw(self.screen)
        self.ghosts.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    heart_game = HeartGame()
    heart_game.run_game()
    # Make a game instance and run it
