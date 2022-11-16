import pygame

class Player:
    """Store the information of a game character"""
    def __int__(self, heart_game):
        self.screen = heart_game.screen
        self.settings = heart_game.settings
        self.screen_rect = heart_game.get_rect()

        self.image = pygame.image.load('images/Icon_Heart.png')
        self.rect =