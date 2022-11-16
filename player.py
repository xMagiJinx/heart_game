import pygame

class Player:
    """Store the information of a game character"""
    def __int__(self, heart_game):
        self.screen = heart_game.screen
        self.settings = heart_game.settings
        self.screen_rect = heart_game.get_rect()

        self.image = pygame.image.load('images/Icon_Heart.png')
        self.rect = self.image.get_rect()

        self.center_heart()

        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the heart and movement"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.heart_speed

    def center_heart(self):
        """Keep the heart at the bottomcenter of the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the heart"""
        self.screen.blit(self.image, self.rect)