from random import randint
import pygame
from pygame.sprite import Sprite
class Flags(Sprite):
    """Store information about the objects to avoid"""
    def __init__(self, heart_game):
        """Initialize the flags"""
        super().__init__()
        self.screen = heart_game.screen
        self.settings = heart_game.settings

        self.image = pygame.image.load('images/Icon_FLag.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        flag_top_max = self.settings.screen_height - self.rect.height
        self.rect.top = randint(0, flag_top_max)

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """update flag positions"""
        self.y += self.settings.flag_speed
        self.rect.y = self.y
