import sys

import pygame

import time
import random
import math
from player import Player
from settings import Settings

class HeartGame:
    """Create a main heart game"""
    def __init__(self):
        """Initialize the game"""
        pygame.init()
        self.settings = Settings()

        self.player = Player(self)

    def run_game(self):
        """Start the main loop to run the game"""
        while True:
            self._check_events()

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

    def _check_keyup_events(self, event):
        """Respond to keyup events"""
        if event.key == pygame.K_RIGHT:
            self.player.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.player.moving_left = False

if __name__ == '__main__':
    heart_game = HeartGame()
    heart_game.run_game()
    # Make a game instance and run it

