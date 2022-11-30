from random import randint
import pygame
from pygame.sprite import Sprite
class Ghosts(Sprite):
    """Store information about the ghost objects to avoid"""
    def __init__(self, heart_game):
        """Initialize the ghosts"""
        super().__init__()
        self.screen = heart_game.screen
        self.settings = heart_game.settings

        self.image = pygame.image.load('images/Icon_Ghost.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        ghost_left_max = self.settings.screen_width - self.rect.width
        self.rect.left = randint(0, ghost_left_max)

        self.x = float(self.rect.x)
        self.y = 0

    def update(self):
        """update ghost positions"""
        self.y += self.settings.ghost_speed
        self.rect.y = self.y
        if not self.screen.get_rect().contains(self.rect):
            self.kill()

