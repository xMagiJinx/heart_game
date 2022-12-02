from random import randint
import pygame
from pygame.sprite import Sprite
class Battery(Sprite):
    """Store information about the battery objects to touch"""
    def __init__(self, heart_game):
        """Initialize the battery"""
        super().__init__()
        self.screen = heart_game.screen
        self.settings = heart_game.settings

        self.image = pygame.image.load('images/Icon_BatteryFull.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        good_left_max = self.settings.screen_width - self.rect.width
        self.rect.left = randint(0, good_left_max)

        self.x = float(self.rect.x)
        self.y = 0

    def update(self):
        """update battery positions"""
        self.y += self.settings.good_speed
        self.rect.y = self.y
        if not self.screen.get_rect().contains(self.rect):
            self.kill()

