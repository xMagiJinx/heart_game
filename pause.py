import pygame
import button

class Pause():
    """This will create a pause menu"""
    def __init__(self, heart_game):
        """Initialize the screen"""
        self.screen = heart_game.screen
        self.settings = heart_game.settings
        self.screen_rect = heart_game.screen.get_rect()

        # self.image = pygame.image.load('images/Item3.png')
        # self.rect = self.image.get_rect()

        # self.rect.center = self.screen_rect.center
        bkg_menu_img = pygame.image.load("images/Item3.png").convert_alpha()

        bkg_button = button.Button(250, 50, bkg_menu_img, 1)

    def draw_text(text, font, text_col, x, y):
        """Render the text"""
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))



