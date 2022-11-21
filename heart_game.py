import sys
from random import random

import pygame

from player import Player
from settings import Settings
from flags import Flags
from game_stats import GameStats

class HeartGame:
    """Create a main heart game"""
    def __init__(self):
        """Initialize the game"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Heart Game")

        self.stats = GameStats(self)

        self.player = Player(self)
        self.flags = pygame.sprite.Group()

    def run_game(self):
        """Start the main loop to run the game"""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.player.update()
                self.create_flags()

            self._update_screen()

    def _check_events(self):
        """Respond to events such as keypresses and mouse"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    def _update_screen(self):
        """Update images on the screen"""
        self.screen.fill(self.settings.bg_color)
        self.player.blitme()

        pygame.display.flip()

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

if __name__ == '__main__':
    heart_game = HeartGame()
    heart_game.run_game()
    # Make a game instance and run it

