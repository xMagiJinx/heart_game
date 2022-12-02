import pygame

class Player:
    """Store the information of a game character"""

    def __init__(self, heart_game):
        """Initialize the game character"""
        self.screen = heart_game.screen
        self.settings = heart_game.settings
        self.screen_rect = heart_game.screen.get_rect()

        self.image = pygame.image.load('images/Icon_Heart.png')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

        self.score_value = 0

    def update(self):
        """Update the heart and movement"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.heart_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.heart_speed
        self.rect.x = self.x
        clock = pygame.time.Clock()
        self.score_value += clock.tick()

    def center_heart(self):
        """Keep the heart at the bottomcenter of the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)


    def blitme(self):
        """Draw the heart"""
        self.screen.blit(self.image, self.rect)
