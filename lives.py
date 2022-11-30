import pygame
from game_stats import GameStats

class Lives:
    """Store and change the amount of lives left"""
    def __init__(self, heart_game):
        """Initialize the game hearts"""
        self.screen = heart_game.screen
        self.settings = heart_game.settings
        self.screen_rect = heart_game.screen.get_rect()
        self.stats = GameStats(self)

        self.image = pygame.image.load('images/Heart.png')

        self.rect = self.image.get_rect()

        self.rect.topright = self.screen_rect.topright

    def update(self, hearts_left):
        """Update which image is shown based off of hearts left"""
        if hearts_left == 2:
            self.image = pygame.image.load('images/Heart2test.png')

        elif hearts_left == 1:
            self.image = pygame.image.load('images/Heart1test.png')
        elif hearts_left == 0:
            self.image = pygame.image.load('images/Heart0test.png')
        else:
            self.image = pygame.image.load('images/Heart.png')

    def blitme(self):
        """Draw the lives"""
        self.screen.blit(self.image, self.rect)